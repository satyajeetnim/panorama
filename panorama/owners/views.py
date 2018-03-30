from flask import Blueprint
from flask_security import login_required

module = Blueprint('owners', __name__)

@module.route('/owner-login')
@login_required
def owner_login():
    return 'Welcome to Owners Profile'