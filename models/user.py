from DB import db

class UserModel(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(256), nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    rsvps = db.relationship("RsvpModel", back_populates="user", lazy="dynamic",cascade="all, delete")
    events = db.relationship("EventModel", back_populates="organizer", lazy="dynamic",cascade="all, delete")


