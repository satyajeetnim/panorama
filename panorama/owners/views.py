from flask import Blueprint

module = Blueprint('owners', __name__)

@module.route('/profile')
def home():
    return 'Welcome to Owners Profile'