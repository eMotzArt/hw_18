from flask_restx import Namespace, Resource, fields

# from app.dao.dao import GenreDAO
from .parser import genre_parser

api = Namespace('genres')

# api model
genre = api.model('Genre', {
    'id': fields.Integer(readonly=True, description='The genre unique pkentifier'),
    'name': fields.String(required=True, description='The genre name')
})

@api.route('/')
class GenresView(Resource):
    @api.marshal_list_with(genre)
    def get(self):
        return


@api.route('/<int:pk>')
class GenreView(Resource):
    @api.marshal_with(genre)
    @api.response(code=404, description='Item not found')
    def get(self, pk):
        return