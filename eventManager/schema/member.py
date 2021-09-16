from marshmallow import fields
from marshmallow import validate

from model import User
from . import ma


class MemberSchema(ma.SQLAlchemySchema):
    class Meta:
        model = User
        load_instance = True
        include_fk = True

    id = ma.auto_field()
    username = ma.auto_field()
    first_name = fields.Str(validate=[validate.Length(max=120)])
    second_name = fields.Str(validate=[validate.Length(max=120)])
