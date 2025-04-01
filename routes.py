from flask import  Blueprint, jsonify, request, g   
from services import GoogleAuthService, FacebookAuthService, TodoService
from repos import TodoRepository
from utils import protected_route, get_user_id, validate_uuid

google_auth = Blueprint("google_auth", __name__, url_prefix="/api/auth/google")
facebook_auth = Blueprint("facebook_auth", __name__, url_prefix="/api/auth/facebook")
todo = Blueprint("todo", __name__, url_prefix="/api/todos/")

google_auth_service = GoogleAuthService()
facebook_auth_service = FacebookAuthService()
todo_service = TodoService()
todo_repository = TodoRepository()


@todo.before_request
def before_request():
    g.google_auth_service = google_auth_service
    g.facebook_auth_service = facebook_auth_service
    g.todo_service = todo_service
    g.todo_repository = todo_repository


@google_auth.before_request
def before_request():
    g.google_auth_service = google_auth_service

@todo.route("/", methods=["GET"])
@protected_route
def get_todos():
    try:
        identifier = request.args.get("identifier")
        user_id = get_user_id(identifier)
        if not user_id:
            raise ValueError("Invalid Registration (You are not registered)")
        todos = g.todo_repository.get_todos(user_id)
        return jsonify({"Success": True, "Todos": todos}), 200
    except Exception as e:
        return jsonify({"Success": False, "Message": str(e)}), 400

@todo.route("/<string:todo_id>", methods=["GET"])
@protected_route
@validate_uuid("todo_id")
def get_todo(todo_id):
    try:
        identifier = request.args.get("identifier")
        user_id = get_user_id(identifier)
        if not user_id:
            raise ValueError("Invalid Registration (You are not registered)")
        todo = g.todo_repository.get_todo(todo_id, user_id)
        return jsonify({"Success": True, "Todo": todo}), 200
    except Exception as e:
        return jsonify({"Success": False, "Message": str(e)}), 400

@todo.route("/", methods=["POST"])
@protected_route
def create_todo():
    data = request.get_json()
    try:
        identifier = request.args.get("identifier")
        user_id = get_user_id(identifier)
        if not user_id:
            raise ValueError("Invalid Registration (You are not registered)")
        todo = g.todo_repository.create_todo(data, user_id)
        return jsonify({"Success": True, "Created Todo": todo}), 201
    except Exception as e:
        return jsonify({"Success": False, "Message": str(e)}), 400


@todo.route("/<todo_id>", methods=["PUT"])
@protected_route
@validate_uuid("todo_id")
def update_todo(todo_id):
    try:
        identifier = request.args.get("identifier")
        user_id = get_user_id(identifier)
        if not user_id:
            raise ValueError("Invalid Registration (You are not registered)")
        todo_data = request.get_json()
        todo = g.todo_repository.update_todo(todo_id, todo_data, user_id)
        return jsonify({"Success": True, "Updated Todo": todo}), 200
    except Exception as e:
        return jsonify({"Success": False, "Message": str(e)}), 400

@todo.route("/<todo_id>", methods=["DELETE"])
@protected_route
@validate_uuid("todo_id")
def delete_todo(todo_id):
    try:
        identifier = request.args.get("identifier")
        user_id = get_user_id(identifier)
        if not user_id:
            raise ValueError("Invalid Registration (You are not registered)")
        g.todo_repository.delete_todo(todo_id, user_id)
        return jsonify({"Success": True, "Message": "Todo deleted successfully"}), 200
    except Exception as e:
        return jsonify({"Success": False, "Message": str(e)}), 400


@google_auth.route("/login", methods=["GET"])
def login():
    return g.google_auth_service.login()

@google_auth.route("/authorised", methods=["GET"])
def authorised():
    return g.google_auth_service.authorised()

@google_auth.route("/logout", methods=["GET"])
def logout():
    return g.google_auth_service.logout()


@facebook_auth.before_request
def before_request():
    g.facebook_auth_service = facebook_auth_service

@facebook_auth.route("/login", methods=["GET"])
def login():
    return g.facebook_auth_service.login()

@facebook_auth.route("/authorised", methods=["GET"])
def authorised():
    return g.facebook_auth_service.authorised()

@facebook_auth.route("/logout", methods=["GET"])
def logout():
    return g.facebook_auth_service.logout()
