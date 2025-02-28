from flask import session, url_for, redirect,jsonify
import os
from models import User
from extensions import db,oauth

class GoogleAuthService:
    def __init__(self): 
        # Initialize the Google OAuth2 client using the oauth object from extensions
        self.google = oauth.register(
            'google',
            client_id=os.getenv('GOOGLE_ID'),
            client_secret=os.getenv('GOOGLE_SECRET'),
            authorize_url='https://accounts.google.com/o/oauth2/auth',
            authorize_params=None,
            access_token_url='https://accounts.google.com/o/oauth2/token',
            refresh_token_url=None,
            client_kwargs={'scope': 'openid profile email'},
        )

    def login(self):
        # Redirect to Google's OAuth2 login
        return self.google.authorize_redirect(url_for('google_auth.authorized', _external=True))

    def authorized(self):
        # Get user info from Google
        token = self.google.authorize_access_token()
        user_info = self.google.get('userinfo')
        
        google_id = user_info.json().get('id')
        # Check if user exists, if not, create a new user
        if User.query.filter_by(google_id=google_id).first() is None:
            user_created = User(google_id=google_id)
            db.session.add(user_created)
            db.session.commit()

        session['user_id'] = google_id
        return jsonify({"success": True, "message": "Successfully logged in"}), 200

    def logout(self):
        session.pop('user_id', None)
        return jsonify({"success": True, "message": "Logged out"}), 200

    def protected_route(self, func):
        """A decorator to protect routes that require Google login"""
        def wrapper(*args, **kwargs):
            if 'user_id' not in session:
                return redirect(url_for('google_auth.login'))
            return func(*args, **kwargs)
        return wrapper