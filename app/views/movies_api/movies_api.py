from flask_restx import Namespace, Resource, fields

# from app.dao.dao import MovieDAO
from .parser import movie_parser, movie_query_parser

api = Namespace('movies')

# api model
movie = api.model('Movie', {
    'id': fields.Integer(readonly=True, description='Movie unique identifier'),
    'title': fields.String(required=True, description='Movie title'),
    'description': fields.String(required=True, description='Movie description'),
    'trailer': fields.String(required=True, description='Movie trailer link'),
    'year': fields.Integer(required=True, description='Movie release year'),
    'rating': fields.Float(required=True, description='Movie rating'),
    'genre_id': fields.Integer(required=True, description='Genre id'),
    'director_id': fields.Integer(required=True, description='Director id')
})

