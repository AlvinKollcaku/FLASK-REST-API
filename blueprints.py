# blueprints.py
from flask_smorest import Api
from resources.event import blp as eventBlueprint
from resources.rsvp import blp as rsvpBlueprint
from resources.tag import blp as tagBlueprint
from resources.user import blp as userBlueprint

def register_blueprints(api: Api):
    api.register_blueprint(eventBlueprint)
    api.register_blueprint(rsvpBlueprint)
    api.register_blueprint(tagBlueprint)
    api.register_blueprint(userBlueprint)
