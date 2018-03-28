import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Flask
APP_DIR = os.path.dirname(os.path.abspath(__file__))

from panorama import public, owners, managers, admin

app = Flask(
    __name__,
    template_folder=os.path.join(APP_DIR, '..', 'templates'),
    )

from panorama.public.views import module
from panorama.owners.views import module
from panorama.managers.views import module
from panorama.admin.views import module

app.register_blueprint(public.views.module)
app.register_blueprint(owners.views.module)
app.register_blueprint(managers.views.module)
app.register_blueprint(admin.views.module)
