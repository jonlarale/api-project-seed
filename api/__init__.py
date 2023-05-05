# Python modules
import os

# Project dependencies
from dotenv import dotenv_values
from flask import Flask
from flask_cors import CORS
from flask_restx import Api

# Global variables
cors = CORS()
config = dotenv_values()
root_api = Api(doc=config.get('SWAGGER_PATH', '/'))

# Local modules
from api.models import init_db
from api.routes.todo import todo_ns
from api.routes.idea import idea_ns
from api.common.db import db_cleanup
from api.common.error_handlers import register_handlers


def create_api():
    app = Flask(__name__)
    app.config.from_mapping(config)
    cors.init_app(app)
    init_db(app)
    root_api.init_app(app)

    # Swagger configuration
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    swagger_path = os.path.join(base_dir, 'templates', 'swagger.html')
    with open(swagger_path, 'r') as f:
        swagger_description = f.read()
    root_api.version = "0.0.1"
    root_api.title = "API"
    root_api.description=swagger_description

    # Here we import the routes/namespaces to register them
    root_api.add_namespace(todo_ns)
    root_api.add_namespace(idea_ns)
    
    # Register error handlers
    register_handlers(app)

    # Register teardown functions
    app.teardown_request(db_cleanup)

    return app
