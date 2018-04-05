from flask import Flask
from flask_bootstrap import Bootstrap
from panorama import public, owners, managers, admin
from panorama.models import User, Role

# Creating Flask app
app = Flask(__name__)

# Initialize flask-bootstrap
Bootstrap(app)

# Load configuration
app.config.from_object('panorama.config.panorama_config')

# MongoEngine initialization
from panorama.models import mongodb
app.db = mongodb
app.db.init_app(app)

# Import and register Blueprints
from panorama.public.views import module
from panorama.owners.views import module
from panorama.managers.views import module
from panorama.admin.views import module

app.register_blueprint(public.views.module)
app.register_blueprint(owners.views.module)
app.register_blueprint(managers.views.module)
app.register_blueprint(admin.views.module)
