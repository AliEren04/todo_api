from flask import Flask
from routes import todo, google_auth, facebook_auth, refresh
from extensions import db, migrate, oauth
from dotenv import load_dotenv
import os
from models import Todo, User
from datetime import timedelta
from flask import jsonify
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_jwt_extended import JWTManager



#Load .env File
load_dotenv()

#App Initialization
app = Flask(__name__)


limiter = Limiter(
    key_func=get_remote_address,
    default_limits=["1000 per day", "200 per hour", "20 per minute", "10 per second"]
)

limiter.init_app(app)

#OAuth Initialization
oauth.init_app(app)


app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SESSION_PERMANENT"] = False
app.config["PERMANENT_SESSION_LIFETIME"] = timedelta(days=365)

#Flask Session Cookies:
# Configuration based on environment variable
if os.getenv("FLASK_ENV") == "development":
    #No Security For Dev environment
    app.config["JWT_COOKIE_SECURE"] = True  
    app.config["JWT_COOKIE_SAMESITE"] = None  
    app.config["JWT_COOKIE_HTTPONLY"] = False  
    print("Development Level No Security.")
else:
    app.config["JWT_COOKIE_SECURE"] = True  # Ensure cookies are only sent over HTTPS
    app.config["JWT_COOKIE_SAMESITE"] = "Lax"  # Lax or Strict for CSRF protection
    app.config["JWT_COOKIE_HTTPONLY"] = True  # Prevent JavaScript from accessing the cookie
    print("Production Level Security Enabled")


app.config["JWT_SECRET_KEY"] = os.getenv('JWT_SECRET_KEY')
app.config['SECRET_KEY'] = os.getenv('FLASK_SECRET_KEY')
jwt = JWTManager(app)
#Extensions Initialization
db.init_app(app)
migrate.init_app(app, db)


#Blueprints Routes
app.register_blueprint(todo)
app.register_blueprint(google_auth)
app.register_blueprint(facebook_auth)
app.register_blueprint(refresh)

#Error Handling
app.errorhandler(404)
def not_found(error):
    return jsonify({"message": "Not Found"}), 404

app.errorhandler(500)
def internal_server_error(error):
    return jsonify({"message": "Internal Server Error"}), 500

if __name__ == "__main__":
    app.run()
