from app.dao import UserDAO


class UserService:
    def __init__(self):
        self.dao = UserDAO()


    def get_users(self, **params):
        return self.dao.get_items()

    def get_user_by_pk(self, pk):
        return self.dao.get_item(pk)

    def add_new_user(self, **data):
        return self.dao.create_item(**data)

    def update_movie(self, pk, **data):
        return self.dao.update_item(pk, **data)

    def delete_movie(self, pk):
        return self.dao.delete_item(pk)
