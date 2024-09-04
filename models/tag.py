from DB import db

class TagModel(db.Model):
    __tablename__ = "tag"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    events=db.relationship("EventModel", back_populates="tags",secondary="event_tag")
    #secondary means that it will populate according to the items_tags table(using it as secondary table)

