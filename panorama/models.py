from flask_mongoengine import MongoEngine
from flask_security import UserMixin, RoleMixin

# Create database connection object
mongodb = MongoEngine()

class Role(mongodb.Document, RoleMixin):
    name = mongodb.StringField(max_length=80, unique=True)
    description = mongodb.StringField(max_length=255)


class User(mongodb.Document, UserMixin):
    email = mongodb.StringField(max_length=255, unique=True)
    name = mongodb.StringField(max_length=255)
    password = mongodb.StringField(max_length=255)
    active = mongodb.BooleanField(default=True)
    confirmed_at = mongodb.DateTimeField()
    roles = mongodb.ListField(mongodb.ReferenceField(Role), default=[])