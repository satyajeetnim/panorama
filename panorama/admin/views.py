from flask import Blueprint

module = Blueprint('admin', __name__)

@module.route('/admin')
def home():
    return 'Welcome to Admin Page'