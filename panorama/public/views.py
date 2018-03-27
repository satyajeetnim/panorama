from flask import Blueprint

module = Blueprint('public', __name__)

@module.route('/')
def home():
    return 'Home'