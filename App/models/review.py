from App.database import db


class Review(db.Model):
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    staff_id: str = db.Column(db.ForeignKey("staff.id"))
    student_id: str = db.Column(db.ForeignKey("student.id"))
    rating: int = db.Column(db.Integer, nullable=False)
    comment: str = db.Column(db.String(200), nullable=False)

    def __init__(
        self, student_id: str, staff_id: str, rating: int, comment: str
    ) -> None:
        self.student_id = student_id
        self.staff_id = staff_id
        self.rating = rating
        self.comment = comment

    def __repr__(self) -> str:
        return f"{self.student_id} - {self.staff_id} - {self.rating} - {self.comment}"
