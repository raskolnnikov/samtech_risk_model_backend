from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

from .config import config_by_name
from flask_cors import CORS, cross_origin


from flask_sqlalchemy import SQLAlchemy as _BaseSQLAlchemy

class SQLAlchemy(_BaseSQLAlchemy):
    def apply_pool_defaults(self, app, options):
        super(SQLAlchemy, self).apply_pool_defaults(app, options)
        options["pool_pre_ping"] = True

db = SQLAlchemy()
flask_bcrypt = Bcrypt()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_by_name['dev'])
    cors = CORS(app, resources={r"/*": {"origins": "*"}})
    db.init_app(app)
    flask_bcrypt.init_app(app)

    return app
