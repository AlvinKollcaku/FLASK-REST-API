from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from flask.views import MethodView #used to create a class, methods of which route to specific endpoints
from flask_smorest import Blueprint,abort
from flask_jwt_extended import jwt_required, get_jwt

from DB import db
from models import EventModel, TagModel, EventsTagsModel
from schemas import TagSchema, EventSchema, EventsTagSchema, PlainTagSchema

# The Blueprint is used to divide the API into multiple segments

blp = Blueprint('Tags', 'tags',description="Operations on tags")

@blp.route("/event/<int:eventId>/tag/<int:tagId>")
class LinkTagToEvent(MethodView):
    @jwt_required()
    @blp.response(200,TagSchema)
    def post(self,eventId,tagId): #Linking an existing tag to an existing event
        event = EventModel.query.get_or_404(eventId)
        tag = TagModel.query.get_or_404(tagId)

        if tag in event.tags:
            abort(400, message="Tag is already linked to this event.")

        event.tags.append(tag)
        try:
            db.session.add(event)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="An error occurred while inserting the tag.")

        return tag

    @jwt_required()
    @blp.response(201, EventsTagSchema)
    def delete(self, book_id, tagId):  # Unlinking a tag to a book

        # 1)Retrieve both components from their respective tables
        event = EventModel.query.get_or_404(book_id)
        tag = TagModel.query.get_or_404(tagId)

        event.tags.remove(tag)

        try:
            db.session.add(event)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="An error occurred while inserting the tag.")

        return {"message": "Book removed from tag", "book": event, "tag": tag}

@blp.route("/tag")
class Tag(MethodView):
    @jwt_required()
    @blp.arguments(TagSchema)
    @blp.response(201,TagSchema)
    def post(self,data): # This creates a tag
        if TagModel.query.filter(TagModel.name == data["name"]).first():
            abort(400, message="A tag with that name already exists.")

        tag = TagModel(**data)

        try:
            db.session.add(tag)
            db.session.commit()
        except SQLAlchemyError as e:
            abort(
                500,
                message=str(e),
            )

        return tag

@blp.route("/tag/<int:tagId>")
class GetTag(MethodView):
    @blp.response(200,TagSchema)
    def get(self, tagId):
        tag = TagModel.query.get_or_404(tagId)

        return tag