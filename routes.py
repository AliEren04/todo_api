from flask import  Blueprint, jsonify, request, g   
from services import GoogleAuthService
from repos import TodoRepository

google_auth = Blueprint("google_auth", __name__, url_prefix="/api/auth/")
todo = Blueprint("todo", __name__, url_prefix="/api/todos/")

google_auth_service = GoogleAuthService()
todo_repository = TodoRepository()


@todo.before_request
def before_request():
    g.google_auth_service = google_auth_service
    g.todo_repository = todo_repository


@google_auth.before_request
def before_request():
    g.google_auth_service = google_auth_service

@todo.route("/", methods=["GET"])
@google_auth_service.protected_route
def get_todos():
    try:
        todos = g.todo_repository.get_todos()
        return jsonify({"Success": True, "Todos": todos}), 200
    except Exception as e:
        return jsonify({"Success": False, "Message": str(e)}), 500

@todo.route("/<todo_id>", methods=["GET"])
@google_auth_service.protected_route
def get_todo(todo_id):
    try:
        todo = g.todo_repository.get_todo(todo_id)
        return jsonify({"Success": True, "Todo": todo}), 200
    except Exception as e:
        return jsonify({"Success": False, "Message": str(e)}), 500

@todo.route("/create", methods=["POST"])
@google_auth_service.protected_route
def create_todo():
    data = request.get_json()
    try:
        todo = g.todo_repository.create_todo(data)
        return jsonify({"Success": True, "Created Todo": todo}), 201
    except Exception as e:
        return jsonify({"Success": False, "Message": str(e)}), 500


@todo.route("/update/<todo_id>", methods=["PUT"])
@google_auth_service.protected_route
def update_todo(todo_id):
    data = request.get_json()
    try:
        todo = g.todo_repository.update_todo(todo_id, data)
        return jsonify({"Success": True, "Updated Todo": todo}), 200
    except Exception as e:
        return jsonify({"Success": False, "Message": str(e)}), 500

@todo.route("/delete/<todo_id>", methods=["DELETE"])
@google_auth_service.protected_route
def delete_todo(todo_id):
    try:
        g.todo_repository.delete_todo(todo_id)
        return jsonify({"Success": True, "Deleted Todo's ID": int(todo_id)}), 200
    except Exception as e:
        return jsonify({"Success": False, "Message": str(e)}), 500


@google_auth.route("/login", methods=["GET"])
def login():
    return g.google_auth_service.login()

@google_auth.route("/authorised", methods=["GET"])
def authorised():
    return g.google_auth_service.authorised()

@google_auth.route("/logout", methods=["GET"])
def logout():
    return g.google_auth_service.logout()
