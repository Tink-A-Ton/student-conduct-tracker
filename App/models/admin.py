from .user import User
from ..database import db


class Admin(User):
    id: str = db.Column(db.String(9), db.ForeignKey("user.id"), primary_key=True)

    def __init__(self, id: str, password: str) -> None:
        super().__init__(id, password)
