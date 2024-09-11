from flask import Flask
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate

import config
from DB import db
from blueprints import register_blueprints
from flask_smorest import Api
from config import config


def create_app(config_name='default'):
    app = Flask(__name__)

    # Load configuration from config file
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db.init_app(app)
    Migrate(app, db)

    api = Api(app)  # Initialize API instance

    # Registering blueprints
    register_blueprints(api)

    jwt = JWTManager(app)

    # Middleware and Error Handlers
    from error_handlers import register_error_handlers
    register_error_handlers(app, jwt)

    return app

app = create_app()

if __name__ == '__main__':
    app.run()