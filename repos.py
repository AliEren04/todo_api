from models import Todo
from schemas import TodoSchema
from flask import jsonify

class TodoRepository:
    def __init__(self):
        self.todo_schema = TodoSchema()
        self.todo_model = Todo()

    def get_todos(self):
        todos = self.todo_model.query.all()
        if not todos:
            return jsonify({"Success": False, "Message": "There are not any todos uploaded"}), 404
        todos_serialized = self.todo_schema.dump(todos)
        return jsonify({"Success": True, "Todos": todos_serialized}), 200
        
    def get_todo(self, todo_id):
        todo = self.todo_model.query.get(todo_id)
        todo_serialized = self.todo_schema.dump(todo)
        if todo:
            return jsonify({"Success": True, "Todo": todo_serialized}), 200
        else:
            return jsonify({"Success": False, "Message": "Todo not found"}), 404

    def create_todo(self, todo):
        todo_serialized = self.todo_schema.dump(todo)
        self.todo_model.create(**todo_serialized)
        self.todo_model.commit()
        return jsonify({"Success": True, "Created Todo": todo_serialized}), 201

    def update_todo(self, todo_id, todo):
        todo_serialized = self.todo_schema.dump(todo)
        self.todo_model.query.get(todo_id).update(todo_serialized)
        self.todo_model.commit()
        return jsonify({"Success": True, "Updated Todo's ID": todo_id, "Updated Todo": todo_serialized}), 200



    def delete_todo(self, todo_id):
        self.todo_model.query.get(todo_id).delete()
        self.todo_model.commit()
        return jsonify({"Success": True, "Deleted Todo's ID": todo_id}), 200