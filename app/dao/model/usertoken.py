from app.database import db

class UserToken(db.Model):
    __tablename__ = 'refreshtokens'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id") )
    refresh_token = db.Column(db.String, nullable=False)
    user = db.relationship("User", backref=db.backref("user"))
