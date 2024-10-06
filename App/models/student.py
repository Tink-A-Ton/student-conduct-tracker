from ..database import db


class Student(db.Model):
    id: str = db.Column(db.String(9), primary_key=True)
    first_name: str = db.Column(db.String(100), nullable=False)
    last_name: str = db.Column(db.String(100), nullable=False)
    programme: str = db.Column(db.String(100), nullable=False)
    reviews = db.relationship("Review", backref="student")

    def __init__(
        self, id: str, first_name: str, last_name: str, programme: str
    ) -> None:
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.programme = programme

    def get_json(self) -> dict[str, str]:
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "programme": self.programme,
        }
