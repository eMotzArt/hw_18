from flask_restx import Namespace, Resource, fields

# from app.dao.dao import DirectorDAO
from .parser import director_parser

api = Namespace('directors')

# api model
director = api.model('Director', {
    'id': fields.Integer(readonly=True, description='Director unique pkentifier'),
    'name': fields.String(required=True, description='The director name')
})
