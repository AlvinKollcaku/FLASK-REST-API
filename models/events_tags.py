from DB import db


class EventsTagsModel(db.Model):
    __tablename__ = "events_tags"

    id = db.Column(db.Integer, primary_key=True)
    event_id = db.Column(db.Integer, db.ForeignKey("event.id"))
    tag_id = db.Column(db.Integer, db.ForeignKey("tag.id"))
