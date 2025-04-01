from functools import wraps
from flask import jsonify, session
from datetime import timedelta, datetime
from models import User
from uuid import UUID

def protected_route(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        access_token = session.get('access_token')
        access_token_expiry = session.get('access_token_expiry')
        user_id = session.get('user_id')
        LEWAY = timedelta(seconds=300)

        if access_token_expiry:
            access_token_expiry = access_token_expiry.replace(tzinfo=None)

        if not user_id or not access_token or datetime.utcnow() > access_token_expiry + LEWAY:
            return jsonify({"success": False, "error": "User not authenticated"}), 401

        return f(*args, **kwargs)

    return decorated_function

def validate_uuid(param_name):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            try:
                if param_name in kwargs:
                    UUID(kwargs[param_name])
                return f(*args, **kwargs)
            except ValueError:
                return jsonify({"Success": False, "Message": f"Invalid UUID format for parameter: {param_name}"}), 400
        return wrapper
    return decorator

def get_user_id(identifier):
    # Check if the identifier matches any of the user identifiers in the database
    user = None
    
    # Check for Google ID
    user = User.query.filter_by(google_id=identifier).first()
    if user:
        return user.id  # Return the user_id if found by google_id
    
    # Check for Facebook ID
    user = User.query.filter_by(facebook_id=identifier).first()
    if user:
        return user.id  # Return the user_id if found by facebook_id
    
    # Check for Email ID
    user = User.query.filter_by(email=identifier).first()
    if user:
        return user.id  # Return the user_id if found by email
    
    # If no match is found, return None
    return None
