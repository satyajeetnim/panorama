from flask import Flask
from flask.ext.mongoalchemy import MongoAlchemy

app = Flask(__name__)
app.config['MONGOALCHEMY_DATABASE'] = 'panorama'
app.config['MONGOALCHEMY_CONNECTION_STRING'] = 'mongodb://localhost:27017/panorama'
db = MongoAlchemy(app)


class Author(db.Document):
    name = db.StringField()


class Book(db.Document):
    title = db.StringField()
    author = db.DocumentField(Author)
    year = db.IntField()