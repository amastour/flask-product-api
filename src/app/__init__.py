from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration



db = SQLAlchemy()


def create_app(config_type='dev'):
    from config import config
    sentry_sdk.init(
        dsn="https://48176c69591e4580b6d69cedb4b09b62@sentry.io/3962456",
        integrations=[FlaskIntegration()]
    )
    app = Flask(__name__)
    app.config.from_object(config[config_type])

    db.init_app(app)

    from .v1 import v1_blueprint
    app.register_blueprint(v1_blueprint, url_prefix='/api/v1')

    

    return app