from flask import request, abort
from .jwt import check_token

def auth_required(rights=None):
    def decor(func):
        def wrapper(*args, **kwargs):
            if 'Authorization' not in request.headers:
                abort(401)

            data = request.headers.get('Authorization')
            token = data.split("Bearer ")[-1]
            if not check_token(token):
                abort(401)

            return func(*args, **kwargs)

        return wrapper
    return decor

