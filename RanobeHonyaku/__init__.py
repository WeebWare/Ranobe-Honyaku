from flask import Flask
from flask_migrate import Migrate

from RanobeHonyaku.database import db
from RanobeHonyaku.admin import admin
from RanobeHonyaku.utils import CONFIG
from RanobeHonyaku.api.v1 import api_v1

app = Flask("RanobeHonyaku")

# Signs cookies so they can't be edited without the key
app.config["SECRET_KEY"] = CONFIG["FLASK"]["SECRET_KEY"]
# We need a database, or we're rip
app.config["SQLALCHEMY_DATABASE_URI"] = CONFIG["FLASK"]["SQLALCHEMY_DATABASE_URI"]
#  Why would I want something like this? (Hint: I don't)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Extension setup (This time around there shouldn't be many of these)
db.init_app(app)
Migrate(app, db)

# Registering the applications blueprints
app.register_blueprint(api_v1)
app.register_blueprint(admin)

# Technically a circular import, but this design pattern is recommended by flask docs
# See: http://flask.pocoo.org/docs/0.11/patterns/packages/
import RanobeHonyaku.views  # noqa
import RanobeHonyaku.handlers # noqa

# Registering our error handlers
for http_code, handler in RanobeHonyaku.handlers.handlers.items():
    app.register_error_handler(http_code, handler)
