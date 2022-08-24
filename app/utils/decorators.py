from flask import request, abort
from .jwt import check_token, decode_token

# Первые декоратор, универсальный:  @auth_required(rights=['uploader', 'admin']) пропустил бы только uploader'a и admin'а
# def auth_required(rights=['user']):
#     def decor(func):
#         def wrapper(*args, **kwargs):
#             if 'Authorization' not in request.headers:
#                 abort(401)
#
#             data = request.headers.get('Authorization')
#             token = data.split("Bearer ")[-1]
#             if not check_token(token):
#                 abort(401)
#
#             user_info = decode_token(token)
#             if not user_info.get('role') in rights:
#                 abort(403)
#
#             return func(*args, **kwargs)
#
#         return wrapper
#     return decor

def authentication():
    if not (bearer_token := request.headers.get('Authorization')):
        abort(401, "Token missed")
    token = bearer_token.split("Bearer ")[-1]
    if not check_token(token):
        abort(401, "Token not valid")
    return token

def authorization(token, rights):
    token_info = decode_token(token)
    if token_info.get('role') in rights:
        return True

def login_required(func):
    def wrapper(*args, **kwargs):
        authentication()
        return func(*args, **kwargs)

    return wrapper


def uploader_permission_required(func):
    rights = ['uploader', 'admin']
    def wrapper(*args, **kwargs):
        token = authentication()
        if not authorization(token, rights):
            abort(403)
        return func(*args, **kwargs)
    return wrapper

def admin_permission_required(func):
    rights = ['admin']
    def wrapper(*args, **kwargs):
        token = authentication()
        if not authorization(token, rights):
            abort(403)
        return func(*args, **kwargs)
    return wrapper
