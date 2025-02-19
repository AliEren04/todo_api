from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_oauthlib.client import OAuth

oauth = OAuth()
db = SQLAlchemy()
migrate = Migrate()