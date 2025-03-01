from flask import Blueprint
from flask import jsonify, request
from services import GoogleAuthService

google_auth = Blueprint("google_auth", __name__, url_prefix="/api/auth/")
todo = Blueprint("todo", __name__, url_prefix="/api/todos/")

google_auth_service = GoogleAuthService()

@todo.route("/view/", methods=["GET"])
@google_auth_service.protected_route
def get_todos():
    return jsonify({"success": True, "todos": []}), 200

@todo.route("/view/<todo_id>", methods=["GET"])
@google_auth_service.protected_route
def get_todo(todo_id):
    if(int(todo_id) == 0):
        return jsonify({"Success": False, "Message": "Todo not found"}), 404
    else: 
        return jsonify({"Success": True, "Todo": todo_id}), 200

@todo.route("/create", methods=["POST"])
@google_auth_service.protected_route
def create_todo():
    data = request.get_json()
    return jsonify({"Success": True, "Created Todo": data}), 201

@todo.route("/update/<todo_id>", methods=["PUT"])
@google_auth_service.protected_route
def update_todo(todo_id):
    data = request.get_json()
    if(int(todo_id) == 0):
        return jsonify({"Success": False, "Message": "Todo not found"}), 404
    else:
        return jsonify({"Success": True, "Updated Todo's ID": int(todo_id), "Updated Todo": data}), 200

@todo.route("/delete/<todo_id>", methods=["DELETE"])
@google_auth_service.protected_route
def delete_todo(todo_id):
    data = request.get_json()
    if(int(todo_id) == 0):
        return jsonify({"Success": False, "Message": "Todo not found"}), 404
    else:
        return jsonify({"Success": True, "Deleted Todo's ID": int(todo_id), "Deleted Todo": data}), 200

@google_auth.route("/login", methods=["GET"])
def login():
    return google_auth_service.login()

@google_auth.route("/authorised", methods=["GET"])
def authorised():
    return google_auth_service.authorised()

@google_auth.route("/logout", methods=["GET"])
def logout():
    return google_auth_service.logout()
