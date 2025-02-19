from models import Todo
from schemas import TodoSchema
from extensions import db
from flask import jsonify

class TodoRepository:
    def __init__(self):
        self.todo_schema = TodoSchema()
        self.todos_schema = TodoSchema(many=True)

    def get_todos(self):
        todos = Todo.query.all()
        return self.todos_schema.dump(todos)
       
        
    def get_todo(self, todo_id):
        todo = Todo.query.filter_by(id=todo_id).first()
        return self.todo_schema.dump(todo)

    def create_todo(self, todo):
        todo_serialized = self.todo_schema.load(todo)
        todo_created = Todo(**todo_serialized)
        db.session.add(todo_created)
        db.session.commit()
        return todo_created

    def update_todo(self, todo_id, todo):
        todo_serialized = self.todo_schema.load(todo)
        Todo.query.filter_by(id=todo_id).update(todo_serialized)
        db.session.commit()
        return todo_id  

    def delete_todo(self, todo_id):
        Todo.query.filter_by(id=todo_id).delete()
        db.session.commit()
        return todo_id