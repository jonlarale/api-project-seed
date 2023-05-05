
# Third party modules
from flask_restx import fields

# Local modules
from api import root_api as api

idea = api.model('Idea', {
    'idea': fields.String(readonly=True, description='Idea task'),
})