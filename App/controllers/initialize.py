import csv
from .admin import create_admin
from .student import create_student
from .staff import create_staff
from .review import create_review
from App.database import db


def initialize() -> None:
    db.drop_all()
    db.create_all()

    with open("App/data/students.csv") as students_file:
        reader = csv.DictReader(students_file)
        for row in reader:
            create_student(
                row["student_id"], row["firstname"], row["lastname"], row["programme"]
            )

    with open("App/data/staff.csv") as staff_file:
        reader = csv.DictReader(staff_file)
        for row in reader:
            create_staff(
                row["staff_id"],
                row["password"],
                row["firstname"],
                row["lastname"],
            )

    with open("App/data/reviews.csv") as reviews_file:
        reader = csv.DictReader(reviews_file)
        for row in reader:
            create_review(
                row["student_id"], row["staff_id"], int(row["rating"]), row["comment"]
            )

    with open("App/data/admin.csv") as reviews_file:
        reader = csv.DictReader(reviews_file)
        for row in reader:
            create_admin(row["admin_id"], row["password"])
