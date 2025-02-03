import uuid

from werkzeug.security import generate_password_hash, check_password_hash
from src.extensions import db
from src.models.base import BaseModel

# ONE - TO - ONE relationship
class User(db.Model, BaseModel):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)

    uuid = db.Column(db.String(255), unique=True, default=lambda: str(uuid.uuid4()))
    
    name = db.Column(db.String(120), nullable=False)
    last_name = db.Column(db.String(120), nullable=False)

    email = db.Column(db.String(120))

    phone_number = db.Column(db.String(120))

    username = db.Column(db.String(120), unique=True, nullable=False)
    _password = db.Column(db.String(255), nullable=False)

    balance = db.Column(db.Float, default=0.0)

    # One-to-Many relationship with Role
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    role = db.relationship('Role', back_populates='users')

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)
    
    def check_permission(self):
        if self.role.is_admin:
            return True
        return False

    def __repr__(self):
        return f"<User ({self.email})>"
    

class Role(db.Model, BaseModel):
    __tablename__ = "roles"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    # One-to-Many relationship with User
    users = db.relationship('User', back_populates='role')

    def __repr__(self):
        return f"{self.name}"