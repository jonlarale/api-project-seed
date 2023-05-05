from requests import Session

# Local imports
from api import config

_session = Session()

def fetch_activity():
    """Fetches a random activity from the Bored API."""
    url = config.get('BORED_API_URL')
    r = _session.get(
        url=f'{url}'
    )
    r.raise_for_status()

    return r.json().get('activity')