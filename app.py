from flask import Flask
from routes import todo, google_auth
from extensions import db, migrate, oauth
from dotenv import load_dotenv
import os
from models import Todo

#App Initialization
app = Flask(__name__)

#OAuth Initialization
oauth.init_app(app)


#Load .env File
load_dotenv()

#Configs From Environment Variables
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SESSION_PERMANENT"] = True
app.secret_key = os.getenv("SECRET_KEY")

#Extensions Initialization
db.init_app(app)
migrate.init_app(app, db)

#Blueprints(Controllers)
app.register_blueprint(todo)
app.register_blueprint(google_auth)

#Error Handling
app.errorhandler(404)
def not_found(error):
    return jsonify({"message": "Not Found"}), 404

app.errorhandler(500)
def internal_server_error(error):
    return jsonify({"message": "Internal Server Error"}), 500

if __name__ == "__main__":
    app.run()
