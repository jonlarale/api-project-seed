# Python libraries
from http import HTTPStatus

# Project dependencies
from flask import Flask

# Local modules
from . import errors

def register_handlers(app: Flask) -> None:

    @app.errorhandler(errors.ThirdPartyError)
    def handle_third_party_error(error: errors.ThirdPartyError):
        return {'message': str(error.message)}, HTTPStatus.SERVICE_UNAVAILABLE

