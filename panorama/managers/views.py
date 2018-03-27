from flask import Blueprint

module = Blueprint('property-managers', __name__)

@module.route('/manager')
def home():
    return 'Welcome to Property Managers Page'