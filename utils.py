from functools import wraps
from flask import jsonify
from uuid import UUID


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



