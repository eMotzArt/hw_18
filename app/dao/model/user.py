import enum

from app.database import db


class RoleEnum(enum.Enum):
    user = 'user'
    uploader = 'uploader'
    admin = 'admin'

    def __str__(self):
        return self.name



class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    role = db.Column(db.Enum(RoleEnum), nullable=False)
