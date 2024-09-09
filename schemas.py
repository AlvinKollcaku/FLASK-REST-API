from marshmallow import Schema, fields, validate

#Here we will define how the object/dict that we will send/receive should look like

class PlainEventSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    capacity=fields.Int(required=True)
    organizer_id = fields.Int(dump_only=True)

class PlainUserSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str(required=True)
    password = fields.Str(required=True, load_only=True)

class PlainRsvpSchema(Schema):
    id = fields.Int(dump_only=True)
    status = fields.Str(required=True,validate=validate.OneOf(["Accept", "Decline", "Tentative"]))

class PlainTagSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)

class EventSchema(PlainEventSchema):
    organizer=fields.Nested(PlainUserSchema(), dump_only=True)
    rsvps=fields.List(fields.Nested(PlainRsvpSchema()), dump_only=True)
    tags=fields.List(fields.Nested(PlainTagSchema()), dump_only=True)

class RsvpSchema(PlainRsvpSchema):
    user_id= fields.Int(required=True)
    event_id= fields.Int(required=True)
    user=fields.Nested(PlainUserSchema(), dump_only=True)
    event=fields.Nested(PlainEventSchema(), dump_only=True)

class TagSchema(PlainTagSchema):
    events = fields.List(fields.Nested(PlainEventSchema()), dump_only=True)

class TagUpdateSchema(Schema):
    name = fields.Str()

class EventsTagSchema(Schema):
    id = fields.Int(dump_only=True)
    event_id = fields.Int(required=True)
    tag_id = fields.Int(required=True)

class EventUpdateSchema(Schema):
    name = fields.Str()
    capacity = fields.Int()

class RsvpUpdateSchema(Schema):
    status = fields.Str(validate=validate.OneOf(["Accept", "Decline", "Tentative"]))

class UserSchema(PlainUserSchema):
    email = fields.Str(required=True, load_only=True)
    rsvps = fields.List(fields.Nested(PlainRsvpSchema()), dump_only=True)
    events = fields.List(fields.Nested(PlainEventSchema()), dump_only=True)