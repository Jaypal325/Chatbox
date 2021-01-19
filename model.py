from appconfig import app,db
import re
from sqlalchemy.orm import validates
from appconfig import bcrypt

class Generic(db.Model):
    __abstract__ = True
    active = db.Column('active', db.String(10), default='Y')
    created = db.Column("created", db.DateTime, default=db.func.current_timestamp())
    modified = db.Column("modified", db.DateTime, default=db.func.current_timestamp(),onupdate=db.func.current_timestamp())

class User(Generic):
    id=db.Column("user_id",db.Integer(),primary_key=True)
    name = db.Column("user_name", db.String(100))
    age = db.Column("user_age", db.Integer())
    email = db.Column("user_email", db.String(100), unique=True)
    password= db.Column("user_password", db.String(100), unique=True)
    loginrefs = db.relationship('Login',uselist=False,backref="userref",lazy=True)


'''@validates('email')
    def validate_email(self, key, email):
        if not email:
            raise AssertionError('No email provided')
        if not re.match("[^@]+@[^@]+\.[^@]+", email):
            raise AssertionError('Provided email is not an email address')
        return email'''

class Login(Generic):
    id = db.Column("id", db.Integer(), primary_key=True)
    email = db.Column("email", db.String(100), unique=True)
    password = db.Column("password", db.String(100), unique=True)
    userid = db.Column('user_id', db.ForeignKey('user.user_id'), unique=False, nullable=True)