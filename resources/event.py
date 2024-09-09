from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from flask.views import MethodView #used to create a class, methods of which route to specific endpoints
from flask_smorest import Blueprint,abort
from flask_jwt_extended import jwt_required, get_jwt, get_jwt_identity

from DB import db
from models import EventModel, TagModel, EventsTagsModel
from schemas import TagSchema, EventSchema, EventsTagSchema, PlainTagSchema, EventUpdateSchema

# The Blueprint is used to divide the API into multiple segments

blp = Blueprint('Events', 'tags',description="Operations on tags")

@blp.route("/event/tag/<int:tag_id>")
class TagInEvent(MethodView):
    @blp.response(200,EventSchema(many=True))
    def get(self, tag_id): # retrieving all events that belong to the tag
        tag = TagModel.query.get_or_404(tag_id)
        events = tag.events
        return events

@blp.route("/event/<int:event_id>")
class Event(MethodView):
    @blp.response(201,EventSchema)
    def get(self, event_id):
        event = EventModel.query.get_or_404(event_id)
        return event

    @jwt_required()
    def delete(self, event_id):
        event = EventModel.query.get_or_404(event_id)
        current_user_id = get_jwt_identity()

        if event.organizer_id != current_user_id:
            abort(403, message="You are not authorized to delete this event.")

        if event.rsvps or event.tags:
            #abort(400, message="Cannot delete an event that has RSVPs or tags associated with it.")
            #if it has rsvps implement the task queue to inform all people who have rsvpd that the
            #event is deleted
            pass

        try:
            db.session.delete(event)
            db.session.commit()
        except SQLAlchemyError:
            db.session.rollback()
            abort(500, message="An error occurred while deleting the event.")

        return {"message": "Event deleted successfully."}

    @jwt_required()
    @blp.arguments(EventUpdateSchema)
    @blp.response(201,EventSchema)
    def put(self, data, event_id):
        event = EventModel.query.get_or_404(event_id)
        current_user_id = get_jwt_identity()

        if event.organizer_id != current_user_id:
            abort(403, message="You are not authorized to update this event.")

        if "name" in data:
            event.name = data["name"]

        if "capacity" in data:
            event.capacity = data["capacity"]

        try:
            db.session.commit()
        except SQLAlchemyError:
            db.session.rollback()
            abort(500, message="An error occurred while updating the event.")

        return event

@blp.route("/event")
class CreateEvent(MethodView):
    @jwt_required()
    @blp.arguments(EventSchema)
    @blp.response(201, EventSchema)
    def post(self, data):
        current_user_id = get_jwt_identity()

        new_event = EventModel(
            name=data["name"],
            capacity=data["capacity"],
            organizer_id=current_user_id
        )
        try:
            db.session.add(new_event)
            db.session.commit()
        except SQLAlchemyError:
            db.session.rollback()
            abort(500, message="An error occurred while creating the event.")

        return new_event




