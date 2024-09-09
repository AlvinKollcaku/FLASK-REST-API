from DB import db

class RsvpModel(db.Model):
    __tablename__ = "rsvp"

    id = db.Column(db.Integer, primary_key=True)
    status=db.Column(db.Enum("Accept","Decline","Tentative"),unique=False,nullable=False)
    user_id = db.Column(
        db.Integer, db.ForeignKey("user.id"), unique=False, nullable=False
    )#the user with who the rsvp is associated with
    event_id = db.Column(
        db.Integer, db.ForeignKey("event.id"), unique=False, nullable=False
    )
    user= db.relationship("UserModel", back_populates="rsvps")
    event=db.relationship("EventModel", back_populates="rsvps")


