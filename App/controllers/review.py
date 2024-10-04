from App.database import db
from App.models import Review
from .staff import get_staff
from .student import get_student


def create_review(student_id: str, staff_id: str, rating: int, comment: str) -> bool:
    if get_student(student_id) is None:
        print("Invalid student ID.")
        return False

    if get_staff(staff_id) is None:
        print("Invalid staff ID.")
        return False

    if rating < 1 or rating > 5:
        print(f"Rating must be between 1 (Very Poor) and 5 (Excellent).\n")
        return False

    review = Review(student_id, staff_id, rating, comment)
    db.session.add(review)
    db.session.commit()
    return True


def get_all_reviews() -> list[Review]:
    return Review.query.all()


def get_review(id: str) -> Review:
    return Review.query.get(id)


def get_student_reviews(student_id: str) -> list[Review]:
    return Review.query.filter_by(student_id=student_id).all()


def get_staff_reviews(staff_id: str) -> list[Review]:
    return Review.query.filter_by(staff_id=staff_id).all()
