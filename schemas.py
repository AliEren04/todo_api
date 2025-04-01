from marshmallow import Schema, fields, validate
from datetime import datetime

class TodoSchema(Schema):
    id = fields.UUID(required=False)
    title = fields.Str(required=True, validate=validate.Length(min=1, max=40))
    description = fields.Str(required=True, validate=validate.Length(min=1, max=255))
    status = fields.Str(required=True, validate=validate.OneOf(["pending", "in progress", "completed"]))
    user_id = fields.UUID(required=True)
    created_at = fields.DateTime(required=False)
    updated_at = fields.DateTime(required=False)

class UserSchema(Schema):
    id = fields.UUID(required=False)
    facebook_id = fields.Str(required=False)
    google_id = fields.Str(required=False)
    email = fields.Str(required=False)
    created_at = fields.DateTime(required=False)
    updated_at = fields.DateTime(required=False)
