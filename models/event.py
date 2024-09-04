from DB import db

class EventModel(db.Model):
    __tablename__ = "event"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    capacity = db.Column(db.Integer, unique=False, nullable=False)
    organizer_id = db.Column(
        db.Integer, db.ForeignKey("user.id"), unique=False, nullable=False
    )
    tags=db.relationship("TagModel", back_populates="events",secondary="event_tag")
    rsvps = db.relationship("RsvpModel", back_populates="event", lazy="dynamic",cascade="all, delete")
    organizer = db.relationship("UserModel", back_populates="events")
