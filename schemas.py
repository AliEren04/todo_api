from marshmallow import Schema, fields, validate

class TodoSchema(Schema):
    id = fields.Int(required=False)
    title = fields.Str(required=True, validate=validate.Length(min=1, max=40))
    description = fields.Str(required=True, validate=validate.Length(min=1, max=255))
    status = fields.Str(required=True, validate=validate.OneOf(["pending", "in progress", "completed"]))
    user_id = fields.Str(required=True)


class UserSchema(Schema):
    id = fields.Int(required=True)
    google_id = fields.Str(required=True, unique=True)
    todos = fields.Nested(TodoSchema, many=True)