from extensions import db

class Todo(db.Model):
    __tablename__ = "todos"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    status = db.Column(db.String(255), nullable=False, default="pending")
    user_id =  db.Column(db.String(255), db.ForeignKey("users.google_id"), nullable=False, index=True) 

    def __repr__(self):
        return f"<Todo {self.id}, Title: {self.title}, Status: {self.status}>"


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    google_id = db.Column(db.String(255), nullable=False, unique= True, index=True)
    todos =  db.relationship("Todo", backref="user", lazy=True)

    def __repr__(self):
        return f"<User {self.id}>"