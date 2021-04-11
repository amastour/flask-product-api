from flask_restplus import fields
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from app import db
from app.v1 import v1_api


class User(db.Model):

    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    public_id = db.Column(db.String(100), unique=True)
    username = db.Column(db.String(64))
    user_role = db.Column(db.String(length=30), default='user')
    password_hash = db.Column(db.String(128))
    is_active = db.Column(db.Boolean, default=False)
    name = db.Column(db.String(64))
    member_since = db.Column(db.DateTime(), default=datetime.now)
    last_seen = db.Column(db.DateTime(), default=datetime.now)

    def hash_password(self, password):
        self.password_hash = pwd_context.encrypt(password)
