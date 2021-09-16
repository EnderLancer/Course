from marshmallow import fields
from marshmallow import validate

from model import Event, EventStatusType
from . import ma
from .artifact import ArtifactSchema
from .guest import GuestSchema


class EventListSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Event
        load_instance = True
        include_fk = True
        fields = ["id", "title", "status"]

    id = ma.auto_field()
    title = fields.Str(required=True, validate=[validate.Length(min=4, max=120)])
    status = fields.Str()


class EventDetailSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Event
        load_instance = True
        include_fk = True
        fields = ["id", "title", "owner_id", "description", "status", "artifacts", "guests"]

    id = ma.auto_field()
    title = fields.Str(required=True, validate=[validate.Length(min=4, max=120)])
    owner_id = ma.auto_field(dump_only=True)
    description = ma.auto_field()
    artifacts = ma.Nested(ArtifactSchema, many=True)
    guests = ma.Nested(GuestSchema, many=True)
    status = fields.Str(validate=[validate.OneOf(EventStatusType.to_list())])
