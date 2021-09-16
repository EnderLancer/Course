from flask import request, make_response
from flask_jwt_extended import create_access_token, set_access_cookies
from flask_restful import Resource
from marshmallow import ValidationError

from model import db
from schema.profile import ProfileSchema


class Registration(Resource):
    def post(self):
        try:
            user = ProfileSchema().load(request.form)
        except ValidationError as err:
            return err.messages
        db.session.add(user)
        db.session.commit()
        response = make_response(ProfileSchema().dump(user))
        set_access_cookies(response, create_access_token(identity=user))
        return response
