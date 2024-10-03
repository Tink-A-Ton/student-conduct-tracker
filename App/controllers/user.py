from App.models import User
from App.database import db


def create_user(id, password) -> User | None:
    existing_user = get_user(id)
    if existing_user:
        return None
    newuser = User(id, password)
    db.session.add(newuser)
    db.session.commit()
    return newuser


def get_user(id) -> User:
    return User.query.get(id)


def get_all_users() -> list[User]:
    return User.query.all()
