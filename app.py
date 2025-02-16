from flask import Flask
from todo import todo
from extensions import db, migrate
from dotenv import load_dotenv
import os
from models import Todo

#App Initialization
app = Flask(__name__)

#Load .env File
load_dotenv()

#Configs From Environment Variables
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["FLASK_RUN_PORT"] = os.getenv("PORT")

#Extensions Initialization
db.init_app(app)
migrate.init_app(app, db)

#Blueprints(Controllers)
app.register_blueprint(todo)

#Welcome Messages To Show Api Is Running Locally(Small Local project with small tweaks wanted can host on render or remotely)
print(f" Welcome to the API!")
print(f"Your API is running on http://localhost:{os.getenv("PORT")}")

if __name__ == "__main__":
    app.run(debug=True)

