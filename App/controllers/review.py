from App.database import db
from App.models import Review
from .staff import get_staff
from .student import get_student


def create_review(student_id: str, staff_id: str, title: str, rating: int, comment: str) -> bool:
    if get_student(student_id) is None:
        print("Invalid student ID.")
        return False

    if get_staff(staff_id) is None:
        print("Invalid staff ID.")
        return False

    if rating < 1 or rating > 10:
        print("Rating must be between 1 (Very Poor) and 10 (Excellent)")
        return False
    
    if title is None or title == "":
        print("Title is required for a review")
        return False

    review = Review(student_id, staff_id, title, rating, comment)
    db.session.add(review)
    db.session.commit()
    return True


def get_all_reviews() -> list[Review]:
    return Review.query.all()


def get_review(id: int) -> Review | None:
    return Review.query.get(id)


def get_student_reviews(student_id: str) -> list[Review]:
    return Review.query.filter_by(student_id=student_id).all()


def get_staff_reviews(staff_id: str) -> list[Review]:
    return Review.query.filter_by(staff_id=staff_id).all()
