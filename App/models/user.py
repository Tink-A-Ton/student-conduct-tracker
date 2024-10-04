from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db


class User(db.Model):
    id: str = db.Column(db.String(9), primary_key=True)
    password: str = db.Column(db.String(120), nullable=False)

    def __init__(self, id: str, password: str) -> None:
        self.id = id
        self.set_password(password)

    def get_json(self) -> dict[str, str]:
        return {"id": self.id}

    def set_password(self, password) -> None:
        """Create hashed password."""
        self.password = generate_password_hash(password)

    def check_password(self, password) -> bool:
        """Check hashed password."""
        return check_password_hash(self.password, password)
