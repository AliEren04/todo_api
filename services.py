from flask import session, url_for, jsonify 
import os
from models import User
from extensions import db, oauth  # oauth is the Authlib OAuth client
from datetime import timedelta, datetime
from functools import wraps

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
            return jsonify({"success": False, "error": f"Failed to initialize Google OAuth2 client: {str(e)}"}), 500

    def login(self):
        # Redirect to Google's OAuth2 login page with offline access to get refresh token
        return self.google.authorize_redirect(url_for('google_auth.authorised', _external=True))

    def authorised(self):
        # Get the token from the OAuth callback
        token = self.google.authorize_access_token()

        refresh_token = token.get('refresh_token')

        # Use the token to fetch user information from Google's userinfo endpoint
        user_info = self.google.get('https://www.googleapis.com/oauth2/v3/userinfo').json()

        google_id = user_info.get('sub')  # 'sub' is the unique Google ID

        # Verify the token: you can make sure that the user has been authenticated by Google
        if not google_id:
            return jsonify({"success": False, "error": "Invalid token or user not authenticated"}), 400

        # Check if the user already exists in the database by Google ID
        user = User.query.filter_by(google_id=google_id).first()

        if user is None:
            # If the user doesn't exist, create a new user
            user = User(google_id=google_id)
            db.session.add(user)
            db.session.commit()
        else:
            # If the user exists, update their access token and refresh token
            user.access_token = token['access_token']
            user.refresh_token = refresh_token

        # Store the Google ID, access token, refresh token, and expiration time in the session
        session['user_id'] = google_id
        session['access_token'] = token['access_token']
        session['refresh_token'] = refresh_token
        
        # Calculate expiration time (current time + expires_in from the token response)
        expires_in = token.get('expires_in', 3600)  # Default to 1 hour if not specified
        session['access_token_expiry'] = datetime.utcnow() + timedelta(seconds=expires_in)

        # Set session lifetime (assuming you've already configured it globally in app config)
        session.permanent = True

        return jsonify({"success": True, "message": "Successfully logged in"}), 200

    def refresh_access_token(self):
        # If the access token has expired, try to refresh it using the refresh token
        refresh_token = session.get('refresh_token')

        if not refresh_token:
            return jsonify({"success": False, "error": "No refresh token available, please log in again"}), 401

        # Use the refresh token to get a new access token from Google
        try:
            new_token = self.google.refresh_token(
                'https://accounts.google.com/o/oauth2/token',
                refresh_token=refresh_token
            )
        except Exception as e:
            return jsonify({"success": False, "error": f"Failed to refresh access token: {str(e)}"}), 500

        # Check if the new token is valid
        if not new_token.get('access_token'):
            return jsonify({"success": False, "error": "Failed to refresh access token, please log in again"}), 401

        # Update the session with the new access token
        session['access_token'] = new_token['access_token']

        # Optionally, update the refresh token if Google issues a new one
        if new_token.get('refresh_token'):
            session['refresh_token'] = new_token['refresh_token']

        return jsonify({"success": True, "message": "Access token refreshed successfully"}), 200


    def is_authenticated(self):
        access_token = session.get('access_token')
        access_token_expiry = session.get('access_token_expiry')
        LEWAY = timedelta(seconds=300)
        
        # Ensure both are naive datetimes
        if access_token_expiry:
            access_token_expiry = access_token_expiry.replace(tzinfo=None)  # Convert to naive
        
        if not access_token or datetime.utcnow() > access_token_expiry + LEWAY:
            return False
        return True

    def protected_route(self, f):
        """Decorator to protect routes with authentication"""
        @wraps(f)
        def decorated_function(*args, **kwargs):
            # Check if the user is authenticated using the `is_authenticated()` method
            if not self.is_authenticated():
                return jsonify({"success": False, "error": "User not authenticated"}), 401
            return f(*args, **kwargs)

        return decorated_function
    
    def logout(self):
        # Clear the session data
        session.pop('user_id', None)
        session.pop('access_token', None)
        session.pop('refresh_token', None)
        session.pop('access_token_expiry', None)
        return jsonify({"success": True, "message": "Logged out successfully"}), 200