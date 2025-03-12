from models import Todo
from schemas import TodoSchema
from extensions import db

class TodoRepository:
    def __init__(self):
        self.todo_schema = TodoSchema()
        self.todos_schema = TodoSchema(many=True)

    def get_todos(self):
        try: 
            todos = Todo.query.all()
            if not todos:
                raise ValueError("No todos found")
            return self.todos_schema.dump(todos)
        except Exception as e:
            raise Exception(f"Failed to get todos: {str(e)}")
            
       
        
    def get_todo(self, todo_id):
        try:
            todo = Todo.query.filter_by(id=todo_id).first()
            if not todo:
                raise ValueError("Todo not found")
            return self.todo_schema.dump(todo)
        except Exception as e:
            raise Exception(f"Failed to get todo: {str(e)}")

    def create_todo(self, todo):
        try:
            todo_serialized = self.todo_schema.load(todo)
            todo_created = Todo(**todo_serialized)
            existing_todo = Todo.query.filter_by(title=todo_created.title, user_id=todo_created.user_id).first()
            if existing_todo:
                raise ValueError("Todo already exists")
            db.session.add(todo_created)
            db.session.commit()
            return self.todo_schema.dump(todo_created)
        except Exception as e:
            raise Exception(f"Failed to create todo: {str(e)}")

    def update_todo(self, todo_id, todo):
        try:
            todo_to_update = Todo.query.filter_by(id=todo_id).first() 
            todo_serialized = self.todo_schema.load(todo, partial=True)
            todo_serialized["id"] = todo_id
            if not todo_to_update:
                raise ValueError("Todo not found")
            if "title" in todo_serialized:
                todo_to_update.title = todo_serialized["title"]
            if "description" in todo_serialized:
                todo_to_update.description = todo_serialized["description"]
            if "status" in todo_serialized:
                if todo_serialized["status"] not in ["pending", "in progress", "completed"]:
                    raise ValueError("Invalid status value")
                todo_to_update.status = todo_serialized["status"]
            if "user_id" in todo_serialized:
                todo_to_update.user_id = todo_serialized["user_id"]
            db.session.commit()
            updated_todo = Todo.query.get(todo_id)
            return self.todo_schema.dump(updated_todo)
        except Exception as e:
            raise Exception(f"Failed to update todo: {str(e)}")

    def delete_todo(self, todo_id):
        try:
            Todo.query.filter_by(id=todo_id).delete()
            db.session.commit()
            return todo_id
        except Exception as e:
            raise Exception(f"Failed to delete todo: {str(e)}")