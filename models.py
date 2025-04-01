from extensions import db
import uuid
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import text

class Todo(db.Model):
    __tablename__ = "todos"
    
    id = db.Column(UUID(as_uuid=True), primary_key=True, server_default=text("gen_random_uuid()"), nullable=False, index=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    status = db.Column(db.String(20), nullable=False, default="pending")
    user_id = db.Column(UUID(as_uuid=True), db.ForeignKey("users.id"), nullable=False, index=True)
    created_at = db.Column(db.DateTime, server_default=text("NOW()"), nullable=False)
    updated_at = db.Column(db.DateTime, server_default=text("NOW()"), onupdate=text("NOW()"), nullable=False)

    def __repr__(self):
        return f"<Todo {self.id}, Title: {self.title}, Status: {self.status}>"

    def to_dict(self):
        return {
            'id': str(self.id),
            'title': self.title,
            'description': self.description,
            'status': self.status,
            'user_id': str(self.user_id),
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }

class User(db.Model):
    __tablename__ = "users"
    
    id = db.Column(UUID(as_uuid=True), primary_key=True, server_default=text("gen_random_uuid()"), nullable=False, index=True)
    facebook_id = db.Column(db.String(255), nullable=True, unique=True, index=True)
    google_id = db.Column(db.String(255), nullable=True, unique=True, index=True)
    email = db.Column(db.String(255), nullable=True, unique=True, index=True)
    todos = db.relationship("Todo", backref="user", lazy=True)
    created_at = db.Column(db.DateTime, server_default=text("NOW()"), nullable=False)
    updated_at = db.Column(db.DateTime, server_default=text("NOW()"), onupdate=text("NOW()"), nullable=False)

    def __repr__(self):
        return f"<User {self.id}>"

    def to_dict(self):
        return {
            'id': str(self.id),
            'facebook_id': self.facebook_id,
            'google_id': self.google_id,
            'email': self.email,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }