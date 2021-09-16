from hashlib import md5

from marshmallow import validate, fields, pre_load

from model import User
from schema import ma


class ProfileSchema(ma.SQLAlchemySchema):
    class Meta:
        model = User
        load_instance = True
        include_fk = True
        fields = ["username", "first_name", "second_name", "email", "password"]

    username = fields.Str(required=True, validate=[validate.Length(max=120)])
    first_name = fields.Str(validate=[validate.Length(max=120)])
    second_name = fields.Str(validate=[validate.Length(max=120)])
    email = fields.Str(required=True, validate=[validate.Email()])
    password = ma.auto_field(load_only=True)

    @pre_load
    def hash_password(self, in_data, **kwargs):
        in_data = in_data.to_dict()
        in_data['password'] = md5(in_data['password'].encode()).hexdigest()
        return in_data
