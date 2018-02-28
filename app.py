from flask import Flask, render_template, flash, redirect, url_for, request, sessions, logging
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt
from flask.ext.pymongo import PyMongo

app = Flask(__name__)
app.config['MONGO_DBNAME'] = 'panorama'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/panorama'
db = PyMongo(app)


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
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email', [validators.Length(min=6, max=50)])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords do not match'),
    ])
    confirm = PasswordField('Confirm Password')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if request.method == 'POST' and form.validate():
        users = app.db.users
        existing_user = users.find_one({'username': request.form['Username']})
        if existing_user is None:
            users.insert({'name': request.form['Name'],
                          'username': request.form['Username'],
                          'email': request.form['Email'],
                          'password': request.form['Password']})
            sessions['username'] = request.form['Username']
            return redirect(url_for('index'))
        return 'That User name already exists!'


    return render_template('register.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
