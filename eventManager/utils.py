from flask import request, make_response

from model import User


def user_token_access(func):
    def wrapper(*args, **kwargs):
        user_token = request.cookies.get("token")
        if user_token:
            user_id_or_code = User.decode_auth_token(request.cookies.get("token"))
            try:
                user_id_or_code = int(user_id_or_code)
            except ValueError:
                return make_response(user_id_or_code)
            response = func(user_id_or_code, *args, **kwargs)
            return response
        else:
            return make_response("You need to login.")
