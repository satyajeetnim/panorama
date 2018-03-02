from flask import Flask, render_template, flash, redirect, url_for, request, session
from wtforms import Form, StringField, PasswordField, validators
from passlib.hash import sha256_crypt
from flask.ext.pymongo import PyMongo
from functools import wraps


app = Flask(__name__)
app.config['MONGO_DBNAME'] = 'panorama'
app.config['MONGO_HOST'] = 'localhost'
app.config['MONGO_PORT'] = 27017
app.config['SECRET_KEY'] = 'abcdxyz321'

mongo = PyMongo(app, config_prefix='MONGO')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def members():
    return render_template('contact.html')


class RegisterForm(Form):
    name = StringField('Name', [validators.Length(min=1, max=50)])
    email = StringField('Email', [validators.Length(min=6, max=50)])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords do not match'),
    ])
    confirm = PasswordField('Confirm Password')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        if not mongo.db.users.find_one({'email': form.email.data}):
            password = sha256_crypt.encrypt(str(form.password.data))
            mongo.db.users.insert({
                'name': form.name.data,
                'email': form.email.data,
                'password': password
            })
            session['email'] = form.email.data
            flash('You are now registered', 'success')
            return redirect(url_for('login'))
        else:
            flash('User with same email exists already', 'danger')
    return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        login_user = mongo.db.users.find_one({'email': request.form['email']})
        if login_user:
            app.logger.info('Existing password: ' + login_user['password'])
            app.logger.info('Password entered by user: ' + request.form['password'])
            if sha256_crypt.verify(request.form['password'], login_user['password']):
                session['email'] = request.form['email']
                session['logged_in'] = True
                flash('Login successful', 'success')
                return redirect(url_for('dashboard'))
            else:
                flash('Password does not match', 'danger')
        else:
            flash('User does not exist. Please register', 'danger')
            return redirect(url_for('register'))

    return render_template('/login.html')


# Check if user logged in
def is_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('Unauthorized, Please login', 'danger')
            return redirect(url_for('login'))
    return wrap


@app.route('/logout')
@is_logged_in
def logout():
    session.clear()
    flash('Successfully logged out', 'success')
    return redirect(url_for('login'))


@app.route('/dashboard')
@is_logged_in
def dashboard():
    return render_template('dashboard.html')

if __name__ == '__main__':
    app.run(debug=True)
