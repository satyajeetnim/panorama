from flask import Blueprint

public = Blueprint('public', __name__)

@public.route('/')
def home():
    return 'Home'