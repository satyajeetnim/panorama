from flask import Flask, render_template, flash, redirect, url_for, request, session
from wtforms import Form, StringField, PasswordField, validators
from passlib.hash import sha256_crypt
from flask.ext.pymongo import PyMongo
from functools import wraps
from flask_googlemaps import GoogleMaps, Map
import requests


app = Flask(__name__)
app.config['MONGO_DBNAME'] = 'panorama'
app.config['MONGO_HOST'] = 'localhost'
app.config['MONGO_PORT'] = 27017
app.config['SECRET_KEY'] = 'abcdxyz321'
app.config['GOOGLEMAPS_KEY'] = 'AIzaSyC0cZY2JZufg0vLzS6iQTF1wXk-Cqy4bpI'

mongo = PyMongo(app, config_prefix='MONGO')
GoogleMaps(app)

GOOGLE_MAPS_API_URL = 'https://maps.googleapis.com/maps/api/geocode/json'



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


class PropertyForm(Form):
    address = StringField('Address', [validators.Length(min=1, max=250)])
    city = StringField('City', [validators.Length(min=1, max=50)])
    state = StringField('State', [validators.Length(min=1, max=50)])
    zip = StringField('Zip', [validators.Length(min=1, max=20)])


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


@app.route('/dashboard', methods=['GET', 'POST'])
@is_logged_in
def dashboard():
    propForm = PropertyForm(request.form)
    properties = list(mongo.db.property.find({'email': session['email']}))
    propMap = Map(
        identifier='propMap',
        lat=37.2581997,
        lng=-104.6549395,
        zoom=4,
        style='height:400px;width:100%;margin:0;'
    )

    for property in properties:
        params = {
            'address': property['property']['address'] + ', ' + property['property']['city'] + ', '
                       + property['property']['state']
                       + ', ' + property['property']['zip'],
            'sensor': 'false',
            'region': 'us',
            'key': 'AIzaSyC0cZY2JZufg0vLzS6iQTF1wXk-Cqy4bpI',
        }

        req = requests.get(GOOGLE_MAPS_API_URL, params=params)
        res = req.json()
        propMap.add_marker(lat=res['results'][0]['geometry']['location']['lat'], lng=res['results'][0]['geometry']['location']['lng'],
                           icon='http://maps.google.com/mapfiles/ms/icons/green-dot.png', infobox=params['address'])


    if request.method == 'POST':
        mongo.db.property.insert(
            {
                'email': session['email'],
                'property': {
                    'address': propForm.address.data,
                    'city': propForm.city.data,
                    'state': propForm.state.data,
                    'zip': propForm.zip.data
                }
        })
        return redirect(url_for('dashboard'))
    return render_template('dashboard.html', form=propForm, properties=properties, propMap=propMap)


if __name__ == '__main__':
    app.run(debug=True)
