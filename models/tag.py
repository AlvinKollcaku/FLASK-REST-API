from DB import db

class TagModel(db.Model):
    __tablename__ = "tag"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    events=db.relationship("EventModel", back_populates="tags",secondary="events_tags")
    #secondary means that it will populate the items_tags table(using it as secondary table)

