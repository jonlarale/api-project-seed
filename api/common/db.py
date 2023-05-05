# Python libraries
from typing import Any

# Local modules
from api.models import db


def db_cleanup(arg: Any) -> None:
    """Remove pending transactions and close connection to the database."""
    print("Cleaning up database session...")
    db.session.rollback()   # Won´t do anything if there are no pending transactions.
    
    db.session.close()
    db.session.remove()
    db.get_engine().dispose()