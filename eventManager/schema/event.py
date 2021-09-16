from datetime import datetime

from marshmallow import fields, validates, ValidationError
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
        fields = ["id", "title", "status", "start_datetime"]

    id = ma.auto_field()
    title = fields.Str(required=True, validate=[validate.Length(min=4, max=120)])
    status = fields.Str()
    start_datetime = fields.DateTime(format='%Y-%m-%d %H:%M:%S')


class EventDetailSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Event
        load_instance = True
        include_fk = True
        fields = ["id", "title", "owner_id", "description", "status", "artifacts", "guests", "start_datetime"]

    id = ma.auto_field()
    title = fields.Str(required=True, validate=[validate.Length(min=4, max=120)])
    owner_id = ma.auto_field(dump_only=True)
    description = ma.auto_field()
    artifacts = ma.Nested(ArtifactSchema, many=True)
    guests = ma.Nested(GuestSchema, many=True)
    status = fields.Str(validate=[validate.OneOf(EventStatusType.to_list())])
    start_datetime = fields.DateTime(format='%Y-%m-%d %H:%M:%S')

    @validates('start_datetime')
    def is_in_future(self, value):
        now = datetime.now()
        if value <= now:
            raise ValidationError("Can't create event in the past!")
