from flask import Blueprint, render_template

module = Blueprint('public', __name__, template_folder='pages')

@module.route('/')
def home():
    return render_template('index.html')


@module.route('/about')
def about():
    return render_template('about.html')


@module.route('/contact')
def contact():
    return render_template('contact.html')