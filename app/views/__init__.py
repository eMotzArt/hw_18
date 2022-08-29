__all__ = ['api']
from flask_restx import Api

from .genres_api.genres_api import api as genres_api
from .directors_api.directors_api import api as directors_api
from .movies_api.movies_api import api as movies_api
from .users_api.users_api import api as users_api
from .auth_api.auth_api import api as auth_api


api = Api()

api.add_namespace(genres_api)
api.add_namespace(directors_api)
api.add_namespace(movies_api)
api.add_namespace(users_api)
api.add_namespace(auth_api)