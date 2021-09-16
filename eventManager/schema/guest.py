import requests
from marshmallow import fields, post_load, validate

from model import Guest, EndpointUrl
from . import ma


class GuestSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Guest
        load_instance = True
        include_fk = True

    id = ma.auto_field()
    first_name = fields.Str(required=True, validate=[validate.Length(max=120)])
    second_name = fields.Str(required=True, validate=[validate.Length(max=120)])
    email = fields.Str(required=True, validate=[validate.Email()], load_only=True)
    occupation_id = ma.auto_field()
    description = fields.Str(default="", required=False)

    @post_load
    def set_guest_description(self, in_data, **kwargs):
        full_name = f'{in_data.first_name} {in_data.second_name}'
        guest_endpoint_list = EndpointUrl.query.filter(
            EndpointUrl.occupation_id == in_data.occupation_id
        ).all()
        for endpoint in guest_endpoint_list:
            search_by_full_name = f"?full_name={full_name}"
            guests = requests.get(endpoint.url + search_by_full_name).json()
            if guests:
                in_data.description = guests[0]['url']
            break
        return in_data
