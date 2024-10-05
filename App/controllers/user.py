from App.models import User
from App.database import db


def create_user(id: str, password: str) -> User | None:
    existing_user: User = get_user(id)
    if existing_user:
        return None
    newuser = User(id, password)
    db.session.add(newuser)
    db.session.commit()
    return newuser


def get_user(id: str) -> User:
    return User.query.get(id)


def get_all_users() -> list[User]:
    return User.query.all()
