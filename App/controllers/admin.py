from ..models import Admin
from App.database import db
from sqlalchemy.exc import SQLAlchemyError


def create_admin(id: str, password: str) -> bool:
    try:
        admin = Admin(id, password)
        db.session.add(admin)
        db.session.commit()
        return True
    except SQLAlchemyError as e:
        db.session.rollback()
        print(f"Error creating admin: {e}")
        return False


def get_admin(id: str) -> Admin | None:
    return Admin.query.get(id)


def get_all_admin() -> list[Admin]:
    return Admin.query.all()


def is_admin(id: str) -> bool:
    return get_admin(id)
