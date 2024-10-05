from datetime import datetime
from App.database import db


class Review(db.Model):
    id: int = db.Column(db.Integer, primary_key=True)
    staff_id: str = db.Column(db.ForeignKey("staff.id"))
    student_id: str = db.Column(db.ForeignKey("student.id"))
    title: str = db.Column(db.String(50), nullable=False)
    rating: int = db.Column(db.Integer, nullable=False)
    comment: str = db.Column(db.String(200), nullable=False)
    created_at: str = db.Column(db.String(25), nullable=False)

    def __init__(
        self, student_id: str, staff_id: str, title: str, rating: int, comment: str
    ) -> None:
        self.student_id = student_id
        self.staff_id = staff_id
        self.title = title
        self.rating = rating
        self.comment = comment
        self.created_at = datetime.now().strftime("%d/%m/%Y, %I:%M %p")

    def get_json(self) -> dict[str, str | int]:
        return {
            "id": self.id,
            "staff_id": self.staff_id,
            "student_id": self.student_id,
            "title": self.title,
            "rating": self.rating,
            "comment": self.comment,
            "created_at": self.created_at,
        }
