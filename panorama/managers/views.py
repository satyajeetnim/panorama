from flask import Blueprint

module = Blueprint('property-managers', __name__)

@module.route('/manager-login')
def manager_login():
    return 'Welcome to Property Managers Page'