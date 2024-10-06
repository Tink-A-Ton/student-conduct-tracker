from ..database import db
from ..models import Student
from sqlalchemy.exc import SQLAlchemyError


def create_student(id: str, first_name: str, last_name: str, programme: str) -> bool:
    try:
        student = Student(id, first_name, last_name, programme)
        db.session.add(student)
        db.session.commit()
        return True
    except SQLAlchemyError as e:
        db.session.rollback()
        print(f"Error creating student: {e}")
        return False


def get_all_students() -> list[Student]:
    return Student.query.all()


def get_student(id: str) -> Student | None:
    return Student.query.get(id)


def get_students_by_name(first_name: str, last_name: str) -> list[Student]:
    return Student.query.filter_by(first_name=first_name, last_name=last_name).all()
