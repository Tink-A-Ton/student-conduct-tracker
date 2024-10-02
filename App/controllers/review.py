from App.database import db
from App.models import Staff, Student, Review
from .staff import get_staff
from .student import get_student


def create_review(student_id: str, staff_id: str, rating: int, comment: str) -> bool:
    staff: Staff | None = get_staff(staff_id)
    student: Student | None = get_student(student_id)

    if student is None:
        print("Invalid student ID.")
        return False

    if staff is None:
        print("Invalid staff ID.")
        return False

    if rating < 1 or rating > 5:
        print(f"Rating must be between 1 (Very Poor) and 5 (Excellent).\n")
        return False

    review = Review(student.id, staff.id, rating, comment)
    db.session.add(review)
    db.session.commit()
    return True


def get_all_reviews() -> list[Review]:
    return Review.query.all()


#  shud prob have better querying
def get_reviews_by_student(student_id: str) -> Review | None:
    reviews: Review | None = Review.query.filter_by(student_id=student_id).first()
    if not reviews:
        print(f"No reviews found for student ID [ {student_id} ]")
        return
    return reviews


def get_reviews_by_staff(staff_id: str) -> Review | None:
    reviews: Review | None = Review.query.filter_by(staff_id=staff_id).first()
    if not reviews:
        print(f"No reviews found for staff ID [ {staff_id} ]")
        return
    return reviews
