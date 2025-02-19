from flask import Flask
from controllers import todo
from extensions import db, migrate
from dotenv import load_dotenv
import os
from models import Todo
from flask_oauthlib.client import OAuth



#App Initialization
app = Flask(__name__)

#OAuth Initialization
oauth = OAuth(app)
google = oauth.remote_app(
    'google',
    consumer_key= os.getenv('GOOGLE_ID'),
    consumer_secret= os.getenv('GOOGLE_SECRET'),
    request_token_params={'scope': 'email profile'},
    base_url='https://www.googleapis.com/oauth2/v1/',
    request_token_url=None,
    access_token_method='POST',
    access_token_url='https://accounts.google.com/o/oauth2/token',
    authorize_url='https://accounts.google.com/o/oauth2/auth',
)

#Load .env File
load_dotenv()

#Configs From Environment Variables
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")

#Extensions Initialization
db.init_app(app)
migrate.init_app(app, db)

#Blueprints(Controllers)
app.register_blueprint(todo)

#Error Handling
app.errorhandler(404)
def not_found(error):
    return jsonify({"message": "Not Found"}), 404

app.errorhandler(500)
def internal_server_error(error):
    return jsonify({"message": "Internal Server Error"}), 500

app.run()

