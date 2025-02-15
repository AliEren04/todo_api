from flask import Flask, jsonify
from controllers.todo import todo
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

app.register_blueprint(todo)

@app.route("/")
def index():
    return jsonify({"success": True, "message": "Welcome to the API!"}), 200

if __name__ == "__main__":
    app.run(debug=True)

