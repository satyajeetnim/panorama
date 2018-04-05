from flask import Blueprint, request, render_template
from panorama.forms import LoginForm, RegisterForm

module = Blueprint('owners', __name__, template_folder='pages')

@module.route('/owner-login', methods=['GET', 'POST'])
def owner_login():
    login_form = LoginForm()
    if request.method == 'POST' and login_form.validate_on_submit():
        pass

    return render_template('login.html', form=login_form)


@module.route('/owner-register', methods=['GET', 'POST'])
def owner_register():
    register_form = RegisterForm()

    if request.method == 'POST' and register_form.validate_on_submit():
        pass

    return render_template('register.html', form=register_form)
