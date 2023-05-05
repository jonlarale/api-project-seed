
# Third party modules
from flask_restx import fields

# Local modules
from api import root_api as api

todo = api.model('Todo', {
    'id': fields.String(readonly=True, description='TODO unique identifier'),
    'task': fields.String(required=True, description='TODO task'),
    'done': fields.Boolean(required=True, description='Status of the task')
})