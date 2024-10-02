from App.models.staff import Staff
from App.database import db
from sqlalchemy.exc import SQLAlchemyError


def create_staff(id: str, password: str, firstname: str, lastname: str) -> bool:
    try:
        staff = Staff(id, password, firstname, lastname)
        db.session.add(staff)
        db.session.commit()
        return True
    except SQLAlchemyError as e:
        db.session.rollback()
        print(f"Error creating staff: {e}")
        return False


def get_staff(id: str) -> Staff | None:
    return Staff.query.get(id)


def get_all_staff() -> list[Staff]:
    return Staff.query.all()
