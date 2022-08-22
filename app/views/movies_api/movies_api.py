from sqlalchemy.exc import IntegrityError
from flask_restx import Namespace, Resource, fields
from .parser import movie_parser, movie_query_parser, movie_parser_with_names
from app.service import MovieService

api = Namespace('movies')

# api model
movie = api.model('Movie', {
    'id': fields.Integer(readonly=True, description='Movie unique identifier'),
    'title': fields.String(required=True, description='Movie title'),
    'description': fields.String(required=True, description='Movie description'),
    'trailer': fields.String(required=False, description='Movie trailer link'),
    'year': fields.Integer(required=True, description='Movie release year'),
    'rating': fields.Float(required=False, description='Movie rating'),
    'genre_id': fields.Integer(required=True, description='Genre id'),
    'director_id': fields.Integer(required=True, description='Director id')
})


@api.route('/')
class MoviesView(Resource):
    @api.response(code=404, description='Movies with this filters not found')
    @api.expect(movie_query_parser)
    @api.marshal_list_with(movie)
    def get(self):
        params = movie_query_parser.parse_args()

        if result := MovieService().get_movies(**params):
            return result, 200
        return '', 404


    @api.expect(movie_parser)
    @api.marshal_with(movie, code=201)
    def post(self):
        data = movie_parser.parse_args()
        return MovieService().add_new_movie(**data)

    @api.expect(movie_parser_with_names)
    @api.marshal_with(movie, code=201)
    def put(self):
        data = movie_parser_with_names.parse_args()
        return MovieService().add_new_movie_with_names(**data)


@api.route('/<int:pk>')
class MovieView(Resource):
    @api.marshal_with(movie)
    @api.response(code=404, description='Item not found')
    def get(self, pk):
        if result := MovieService().get_movie_by_pk(pk):
            return result, 200
        return '',404

    @api.expect(movie_parser)
    @api.response(code=204, description="Successfully modified")
    def put(self, pk):
        data = movie_parser.parse_args()
        return MovieService().update_movie(pk, **data), 201

    @api.response(code=204, description="Successfully deleted")
    def delete(self, pk):
        MovieService().delete_movie(pk)
        return None, 204

    @api.errorhandler(IntegrityError)
    def handle_exception(error):
        message = f"Error: {error.orig} with params: {error.params}"
        return {'message': message}, 500