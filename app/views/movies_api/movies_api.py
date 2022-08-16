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

@api.route('/')
class MoviesView(Resource):
    @api.expect(movie_query_parser)
    @api.marshal_list_with(movie)
    def get(self):
        return

    @api.expect(movie_parser)
    @api.marshal_with(movie, code=201)
    def post(self):
        return


@api.route('/<int:pk>')
class MovieView(Resource):
    @api.marshal_with(movie)
    @api.response(code=404, description='Item not found')
    def get(self, pk):
        return

    @api.expect(movie_parser)
    @api.response(code=204, description="Successfully modified")
    def put(self, pk):
        return

    @api.response(code=204, description="Successfully deleted")
    def delete(self, pk):
        return
