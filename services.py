from flask import url_for, jsonify 
import os
from models import User
from extensions import db, oauth  # oauth is the Authlib OAuth client
from datetime import timedelta, datetime
import uuid
from repos import TodoRepository
from flask_jwt_extended import create_access_token, create_refresh_token

class GoogleAuthService:
    def __init__(self): 
        # Initialize the Google OAuth2 client using Authlib's OAuth object
        try:
            self.google = oauth.register(
                'google',
                client_id=os.getenv('GOOGLE_ID'),
                client_secret=os.getenv('GOOGLE_SECRET'),
                refresh_token_url=None,
                client_kwargs={'scope': 'profile email openid', 'access_type': 'offline'},
                server_metadata_url='https://accounts.google.com/.well-known/openid-configuration'
            )
        except Exception as e:
            raise RuntimeError(f"Failed To Initialise GoogleAuth Service Class {str(e)}") from e

    def login(self):
        # Redirect to Google's OAuth2 login page with offline access to get refresh token
        return self.google.authorize_redirect(url_for('google_auth.authorised', _external=True))

    def authorised(self):
        
        try:
        # Get the token from the OAuth callback
            token = self.google.authorize_access_token()
            if not token:
                return jsonify({"success": False, "error": f"Invalid token or user not authenticated "}), 400
        except Exception as e:
            return jsonify({"success": False, "error": f"Authentication Failed Details: {str(e)}"}), 400
    
       
        try:
        # Use the token to fetch user information from Google's userinfo endpoint
            
            user_info = self.google.get('https://www.googleapis.com/oauth2/v3/userinfo').json()
        
        except Exception as e:
            return jsonify({"success": False, "error": f"Failed to fetch Google user info: {str(e)}"}), 500

        google_id = user_info.get('sub')  # 'sub' is the unique Google ID

        # Verify the token: you can make sure that the user has been authenticated by Google
        if not google_id:
            return jsonify({"success": False, "error": "Invalid token or user not authenticated"}), 400
        
           
        def generate_random_id():
            return str(uuid.uuid4())
        
        try: 
        # Check if the user already exists in the database by Google ID
            user = User.query.filter_by(google_id=google_id).first()

            if user is None:
            # If the user doesn't exist, create a new user
                user = User(google_id=google_id, id=generate_random_id())
                db.session.add(user)
                db.session.commit()
            
        except Exception as e:
            db.session.rollback() # Rollback the session in case of database error
            return jsonify({"success": False, "error": f"Database error during user management: {str(e)}"}), 500
        
        try:
            access_token = create_access_token(identity=user.id, fresh=True, expires_delta=timedelta(hours=3))
            refresh_token = create_refresh_token(identity=user.id, expires_delta= timedelta(days=30))
        except Exception as e: 
            return jsonify({"success": False, "error": f"Token Creation Related Error: {str(e)}"}), 500
        
           

        return jsonify({
            "success": True,
            "access_token": access_token,
            "refresh_token": refresh_token,
            "message": "Successfully logged in"
        }), 200
    



class FacebookAuthService:
    def __init__(self):
        try:
            self.facebook = oauth.register(
            'facebook',
            client_id=os.getenv('FACEBOOK_ID'),
            client_secret=os.getenv('FACEBOOK_SECRET'),
            authorize_url='https://www.facebook.com/v22.0/dialog/oauth',  # Explicitly specify the URL
            api_base_url='https://graph.facebook.com/v22.0/',
            access_token_url='https://graph.facebook.com/v22.0/oauth/access_token',
            refresh_token_url=None,
            client_kwargs={'scope': 'email public_profile', 'access_type': 'offline'},
        )
        except Exception as e:
            raise RuntimeError(f"Failed To Initialise GoogleAuth Service Class {str(e)}") from e

    def login(self):
        # Redirect to Facebook's OAuth2 login page with offline access to get refresh token
        return self.facebook.authorize_redirect(url_for('facebook_auth.authorised', _external=True))


    def authorised(self, ):
       
        try:
            token = self.facebook.authorize_access_token()
            if token is None:
                return jsonify({"success": False, "error": "Failed to get access token"}), 400
        
            if "access_token" not in token:
                return jsonify({"success": False, "error": "Failed to get access token"}), 400

        except Exception as e: 
             return jsonify({"success": False, "error": f"Authentication Failed Details: {str(e)}"}), 400    
        
        
        user_info_response = self.facebook.get("me?fields=email,name")  # Only fetching email and name
        user_info = user_info_response.json()  # Convert the response to JSON

        if not user_info:
            return jsonify({"success": False, "error": "Failed to fetch user info from Facebook"}), 400

        facebook_id = user_info.get("id")

        if not facebook_id:
            return jsonify({"success": False, "error": "Facebook ID is required"}), 400

        def generate_random_id():
            return str(uuid.uuid4())
        try:
            user = User.query.filter_by(facebook_id=facebook_id,).first()
            if user is None:
                user = User(facebook_id=facebook_id, id=generate_random_id())
                db.session.add(user)
                db.session.commit()
        except Exception as e:
            db.session.rollback()
            return jsonify({"success": False, "error": f"Database error during user management: {str(e)}"}), 500
        try:
            access_token = create_access_token(identity=user.id, fresh=True, expires_delta=timedelta(hours=3))
            refresh_token = create_refresh_token(identity=user.id, expires_delta=timedelta(days=30))
        except Exception as e:
            return jsonify({"success": False, "error": f"Token Creation Related Error: {str(e)}"}), 500
        
        return jsonify({
            "success": True,
            "access_token": access_token,
            "refresh_token": refresh_token,
            "message": "Successfully logged in"
        }), 200

        
class TodoService:
    def __init__(self):
        self.todo_repository = TodoRepository()

    def get_todos(self, user_id):
        return self.todo_repository.get_todos(user_id)

    def get_todo(self, todo_id, user_id):
        return self.todo_repository.get_todo(todo_id, user_id)

    def create_todo(self, todo_data, user_id):
        return self.todo_repository.create_todo(todo_data, user_id)

    def update_todo(self, todo_id, todo_data, user_id):
        return self.todo_repository.update_todo(todo_id, todo_data, user_id)

    def delete_todo(self, todo_id, user_id):
        return self.todo_repository.delete_todo(todo_id, user_id)
    
