from flask_restx import Resource, Namespace

from api.models import db
from api import root_api as api
from api.models.todo import TodoModel
from api.schemas.todo import todo
from api.common import errors


todo_ns = Namespace(name='todos', description='TODO operations')

@todo_ns.route('/')
class TodoList(Resource):
    @todo_ns.marshal_list_with(todo)
    def get(self):
        return TodoModel.query.all()

    @todo_ns.expect(todo)
    @todo_ns.marshal_with(todo, code=201)
    def post(self):
        new_todo = TodoModel(task=api.payload['task'], done=api.payload['done'])
        db.session.add(new_todo)
        db.session.commit()
        return new_todo, 201

@todo_ns.route('/<string:id>')
class Todo(Resource):
    @todo_ns.marshal_with(todo)
    def get(self, id):
        todo = TodoModel.query.get(id)
        if todo:
            return todo
        raise errors.ResourceNotFound(f"TODO {id} not found.")

    @todo_ns.expect(todo)
    @todo_ns.marshal_with(todo)
    def put(self, id):
        todo = TodoModel.query.get(id)
        if todo:
            todo.task = api.payload['task']
            todo.done = api.payload['done']
            db.session.commit()
            return todo
        raise errors.ResourceNotFound(f"TODO {id} not found.")

    def delete(self, id):
        todo = TodoModel.query.get(id)
        if todo:
            db.session.delete(todo)
            db.session.commit()
            return '', 204
        raise errors.ResourceNotFound(f"TODO {id} not found.")
    
