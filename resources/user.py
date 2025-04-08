import requests,os
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from marshmallow import Schema,fields
from passlib.hash import pbkdf2_sha256
from sqlalchemy.exc import SQLAlchemyError
from flask_jwt_extended import create_access_token,create_refresh_token,get_jwt_identity, jwt_required, get_jwt

from DB import db
from models import UserModel
from schemas import UserSchema, PlainUserSchema
from blocklist import BLOCKLIST

class LoginSchema(Schema):
    access_token = fields.Str(required=True)
    refresh_token = fields.Str(required=True)

blp = Blueprint("Users", "users", description="Operations on users")

@blp.route("/register")
class UserRegister(MethodView):
    @blp.arguments(UserSchema)
    def post(self,user_data):
        if UserModel.query.filter(UserModel.username == user_data["username"]).first():
            abort(409, message="A user with that username already exists.")
        #can also catch IntegrityError to avoid this

        user = UserModel(
            username=user_data["username"],
            password=pbkdf2_sha256.hash(user_data["password"]),
            email=user_data["email"]
        )
        db.session.add(user)
        db.session.commit()

        try:
            db.session.add(user)
            db.session.commit()
        except SQLAlchemyError:
            abort(400,message="Something went wrong when registering the user")

        return {"message": "User registered successfully."} , 201

@blp.route("/user/<int:user_id>")
class User(MethodView):
    @blp.response(200,UserSchema)
    def get(self, user_id):
        user = UserModel.query.get(user_id)
        return user

    @jwt_required()
    def delete(self, user_id):
        user = UserModel.query.get_or_404(user_id)
        current_user_id = int(get_jwt_identity())

        if str(user.id) != str(current_user_id):
            abort(403, message="You are not authorized to delete this account.")
        try:
            db.session.delete(user)
            db.session.commit()
        except SQLAlchemyError:
            abort(400,message="Something went wrong when deleting the user")

        return {"message": "User deleted successfully."} , 200

@blp.route("/login")
class UserLogin(MethodView):
    @blp.arguments(PlainUserSchema)
    def post(self, user_data):
        user = UserModel.query.filter(UserModel.username == user_data["username"]).first()

        if user and pbkdf2_sha256.verify(user_data["password"], user.password):
            access_token = create_access_token(identity=str(user.id), fresh=True)
            return {"access_token": access_token}, 200

        abort(401, message="Invalid credentials.")

@blp.route("/logout")
class UserLogout(MethodView):
    @jwt_required()
    def post(self):
        jti = get_jwt()["jti"]
        BLOCKLIST.add(jti)
        return {"message": "Successfully logged out"}, 200






