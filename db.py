from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['MONGO_DBNAME'] = 'panorama'
app.config['MONGO_HOST'] = 'localhost'
app.config['MONGO_PORT'] = 27017

mongo = PyMongo(app, config_prefix='MONGO')

with app.app_context():
    mongo.db.users.insert({'name': 'Satyajeet',
                           'username': 'satyajeetnim',
                           'email': 'satyajeetnim@gmail.com'})

if __name__ == '__main__':
    app.run(debug=True)
