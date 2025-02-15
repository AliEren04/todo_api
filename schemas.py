from marshmallow import Schema, fields

class TodoSchema(Schema):
    id = fields.Int(required=True)
    title = fields.Str(required=True validate=validate.Length(min=1, max=40))
    description = fields.Str(required=True validate= validate.Length(min=1, max=255))
    status = fields.Str(required=True)