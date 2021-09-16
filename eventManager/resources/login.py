from flask import request, make_response
from flask_jwt_extended import create_access_token, set_access_cookies, current_user, jwt_required
from flask_restful import Resource

from model import User
from schema.profile import ProfileSchema


class Login(Resource):
    @jwt_required()
    def get(self):
        return ProfileSchema().dump(current_user)

    def post(self):
        user = User.login(username=request.form.get('username'),
                          password=request.form.get('password'))
        response = make_response(ProfileSchema().dump(user))
        set_access_cookies(response, create_access_token(identity=user))
        return response
