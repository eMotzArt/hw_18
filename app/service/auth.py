from flask import abort
from app.dao import AuthDAO
from app.utils import is_passwords_equals, get_hash
from app.utils import generate_tokens, decode_token

class AuthService:
    def __init__(self):
        self.dao = AuthDAO()


    def get_tokens_by_login_password(self, **data):
        user_name = data.get('username', None)
        user_password = data.pop('password', None)

        if None in [user_name, user_password]:
            abort(400)

        user = self.dao.get_user_by_name(user_name)

        if not is_passwords_equals(get_hash(user_password), user.password):
            abort(401)

        data['role'] = str(user.role)
        data['user_id'] = user.id
        tokens = generate_tokens(**data)
        self.dao.record_refresh_token(user.id, tokens['refresh_token'])
        return tokens

    def get_tokens_by_refresh_token(self, **data):
        refresh_token = data.pop('refresh_token')
        user_info = decode_token(refresh_token)
        user_id = user_info.get('user_id')
        # TO DO сверить с базой токенов, сгенерить, записать, вернуть токены

        if not self.dao.compare_refresh_tokens(user_id, refresh_token):
            abort(401)

        user_info.pop('exp')
        tokens = generate_tokens(**user_info)
        self.dao.record_refresh_token(user_id, tokens['refresh_token'])
        return tokens

