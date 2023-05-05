from flask_restx import Resource, Namespace

# Local imports
from api.schemas.idea import idea
from api.common import errors
from api.services import boredapi


idea_ns = Namespace(name='ideas', description='If you don\'t have any todo, you can get an idea here.')

@idea_ns.route('/')
class Idea(Resource):
    @idea_ns.marshal_with(idea)
    def get(self):
        """Get a random idea."""
        if (activity := boredapi.fetch_activity()) is None:
            raise errors.ThirdPartyError(message='No activity found.')
        return {'idea': activity}
