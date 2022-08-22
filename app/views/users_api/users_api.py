from flask_restx import Namespace, Resource, fields
from app.views.users_api.parser import user_parser
from app.service import UserService

api = Namespace('users')

# api model
user = api.model('User', {
    'id': fields.Integer(readonly=True, description='User unique identifier'),
    'username': fields.String(required=True, description='User name'),
    'password': fields.String(required=True, description='User password'),
    'role': fields.String(required=True, description='User role')
})

@api.route('/')
class UsersView(Resource):
    @api.marshal_list_with(user)
    def get(self):
        return UserService().get_users()

    @api.expect(user_parser)
    @api.marshal_with(user, code=201)
    def post(self):
        return

@api.route('/<int:pk>/')
class UserView(Resource):
    @api.marshal_with(user)
    @api.response(code=404, description='User with this pk is not found in database')
    def get(self, pk):
        # if result := DirectorService().get_director_by_pk(pk):
        #     return result, 200
        return '', 404

    @api.expect(user_parser)
    @api.response(code=204, description="Successfully modified")
    @api.marshal_with(user)
    def put(self, pk):
        # data = movie_parser.parse_args()
        return # MovieDAO().update_item(pk, **data), 201

    @api.response(code=204, description="Successfully deleted")
    def delete(self, pk):
        # MovieDAO().delete_item(pk)
        return None, 204