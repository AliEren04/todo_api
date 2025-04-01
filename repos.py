from models import Todo
from schemas import TodoSchema
from extensions import db
from sqlalchemy.exc import IntegrityError
from uuid import UUID

class TodoRepository:
    def __init__(self):
        self.todo_schema = TodoSchema()
        self.todos_schema = TodoSchema(many=True)

    def get_todos(self, user_id: UUID):
        try: 
            todos = Todo.query.filter_by(user_id=user_id).all()
            if not todos:
                raise ValueError("No todos found")
            return self.todos_schema.dump(todos)
        except Exception as e:
            raise Exception(f"Failed to get todos: {str(e)}")
            
    def get_todo(self, todo_id: UUID, user_id: UUID):
        try:
            todo = Todo.query.filter_by(id=todo_id, user_id=user_id).first()
            if not todo:
                raise ValueError("Todo not found")
            return self.todo_schema.dump(todo)
        except Exception as e:
            raise Exception(f"Failed to get todo: {str(e)}")

    def create_todo(self, todo: dict, user_id: UUID):
        try:
            if not todo:
                raise ValueError("Invalid todo data")
            if user_id is None:
                raise ValueError("User ID is required")

            todo_serialized = self.todo_schema.load(todo)   
            todo_created = Todo(**todo_serialized)
            db.session.add(todo_created)
            db.session.commit()
            return self.todo_schema.dump(todo_created)
        except IntegrityError as e:
            db.session.rollback()
            raise ValueError(f"Database constraint violation: {str(e)}")
        except Exception as e:
            db.session.rollback()
            raise Exception(f"Failed to create todo: {str(e)}")

    def update_todo(self, todo_id: UUID, todo: dict, user_id: UUID):
        try:
            todo_to_update = Todo.query.filter_by(id=todo_id, user_id=user_id).first() 
            todo_serialized = self.todo_schema.load(todo, partial=True)
            todo_serialized["id"] = todo_id

            if user_id is None:
                raise ValueError("User ID is required")

            if not todo_to_update:
                raise ValueError(f"Todo not found by specified id ({todo_id}) please provide valid todo_id")
            for key, value in todo_serialized.items():
                setattr(todo_to_update, key, value)
            db.session.commit()
            updated_todo = Todo.query.get(todo_id)
            return self.todo_schema.dump(updated_todo)
        except IntegrityError as e:
            db.session.rollback()
            raise ValueError(f"Database constraint violation: {str(e)}")
        except Exception as e:
            db.session.rollback()
            raise Exception(f"Failed to update todo: {str(e)}")

    def delete_todo(self, todo_id: UUID, user_id: UUID):
        try:
            todo_to_delete = Todo.query.filter_by(id=todo_id, user_id=user_id).first()
            if not todo_to_delete:
                raise ValueError(f"Todo not found by specified id ({todo_id}) please provide valid todo_id")
            db.session.delete(todo_to_delete)
            db.session.commit()
            return todo_id
        except Exception as e:
            raise Exception(f"Failed to delete todo: {str(e)}")