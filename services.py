from extensions import oauth
from dotenv import load_dotenv
from flask import jsonify, session, url_for
import os

load_dotenv()

class GoogleAuthService():
    def __init__(self): 
        self.oauth = oauth
        self.google = oauth.remote_app(
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
    
    def login(self):
        return self.google.authorize(callback=url_for('google.authorized', _external=True))

    def authorised(self):
        try:
            response = self.google.authorized_response()
            if response is None or response.get('access_token') is None:
                return jsonify({"success": False, "message": "Authorization failed"}), 401
            session['access_token'] = (response['access_token'])
            return jsonify({"success": True, "message": "Authorized"}), 200
        except Exception as e:
            return jsonify({"success": False, "message": "Authorization failed", "details": str(e)}), 401


    def logout(self):
        session.pop('access_token', None)
        return jsonify({"success": True, "message": "Logged out"}), 200

    

    
