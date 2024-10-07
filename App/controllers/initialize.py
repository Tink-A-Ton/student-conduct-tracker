import csv
from ..database import db
from .admin import create_admin
from .student import create_student
from .staff import create_staff
from .review import create_review


def initialize() -> None:
    db.drop_all()
    db.create_all()

    with open("App/data/students.csv") as students_file:
        reader = csv.DictReader(students_file)
        for row in reader:
            create_student(
                id=row["student_id"], 
                first_name=row["firstname"], 
                last_name=row["lastname"], 
                programme=row["programme"]
            )

    with open("App/data/staff.csv") as staff_file:
        reader = csv.DictReader(staff_file)
        for row in reader:
            create_staff(
                id=row["staff_id"],
                password=row["password"],
                firstname=row["firstname"],
                lastname=row["lastname"],
            )

    with open("App/data/reviews.csv") as reviews_file:
        reader = csv.DictReader(reviews_file)
        for row in reader:
            create_review(
                student_id=row["student_id"],
                staff_id=row["staff_id"],
                title=row["title"],
                rating=int(row["rating"]),
                comment=row["comment"]
            )

    with open("App/data/admin.csv") as reviews_file:
        reader = csv.DictReader(reviews_file)
        for row in reader:
            create_admin(
                id=row["admin_id"],
                password=row["password"]
            )
