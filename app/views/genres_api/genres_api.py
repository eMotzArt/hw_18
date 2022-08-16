from flask_restx import Namespace, Resource, fields

# from app.dao.dao import GenreDAO
from .parser import genre_parser

api = Namespace('genres')

# api model
genre = api.model('Genre', {
    'id': fields.Integer(readonly=True, description='The genre unique pkentifier'),
    'name': fields.String(required=True, description='The genre name')
})
