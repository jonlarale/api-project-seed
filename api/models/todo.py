# Python modules
from uuid import uuid4

# Project dependencies
from sqlalchemy.sql import func

# Local modules
from api.models import db

class BaseModel(db.Model):
    """Base model."""

    __abstract__ = True

    id = db.Column(
        db.String(36),
        primary_key=True,
        default=lambda: str(uuid4())
    )
    created_at = db.Column(
        db.DateTime(),
        nullable=False,
        server_default=func.now()
    )
    updated_at = db.Column(
        db.DateTime(),
        nullable=False,
        server_default=func.now(),
        onupdate=func.now()
    )

class TodoModel(BaseModel):
    """Todo model."""
    task = db.Column(db.String(100), nullable=False)
    done = db.Column(db.Boolean, nullable=False)

    def __repr__(self):
        return f"<Todo {self.id}: {self.task}>"