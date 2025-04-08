from flask import Flask
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate

import config
from DB import db
from blueprints import register_blueprints
from flask_smorest import Api
from config import Config
from error_handlers import register_error_handlers


def create_app(config_name='default'):
    app = Flask(__name__)

    app.config.from_object(Config) #don't use dict for object injection->simply use classes
    #config[config_name].init_app(app)

    db.init_app(app)
    Migrate(app, db)

    api = Api(app)  # Initialize API instance

    # Registering blueprints
    register_blueprints(api)

    jwt = JWTManager(app)

    # Middleware and Error Handlers
    register_error_handlers(app, jwt)

    return app

app = create_app()

if __name__ == '__main__':
    app.run()