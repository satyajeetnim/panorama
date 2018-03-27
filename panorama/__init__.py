from flask import Flask

from panorama import public, owners, managers, admin

app = Flask(__name__)

from panorama.public.views import module
from panorama.owners.views import module
from panorama.managers.views import module
from panorama.admin.views import module

app.register_blueprint(public.views.module)
app.register_blueprint(owners.views.module)
app.register_blueprint(managers.views.module)
app.register_blueprint(admin.views.module)
