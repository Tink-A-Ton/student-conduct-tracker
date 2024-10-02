import click
from flask.cli import AppGroup
from App.database import get_migrate
from App.main import create_app
from App.models import Student, Staff
from App.controllers import (
    initialize,
    get_all_students,
    get_student,
    get_students_by_name,
)

app = create_app()
migrate = get_migrate(app)


@app.cli.command("init", help="Creates and initializes the database")
def init():
    initialize()
    print("database intialized")


student_cli = AppGroup("student", help="Student object commands")


@student_cli.command("list-all", help="List all students")
def list_students_command() -> None:
    students: list[Student] = get_all_students()
    if not students:
        print("There are currently no students registered.")
    else:
        print(students)


# This command searches for and displays a student in the database based on ID
# flask student search-id
@student_cli.command("search-id", help="Search for a student by ID")
def get_student_by_id_command() -> None:
    student_id: str = click.prompt(text="Enter Student ID", type=str)
    student: Student | None = get_student(student_id)
    if student:
        print(student)


# This command searches for and displays a student in the database based on name
# flask student search-name
@student_cli.command("search-name", help="Search for students by name")
def get_student_by_name_command() -> None:
    first_name: str = click.prompt(text="Enter first_name")
    last_name: str = click.prompt(text="Enter last_name")
    students: list[Student] = get_students_by_name(first_name, last_name)
    if students:
        print(students)


@student_cli.command("view-reviews", help="View a student's reviews")
def get_student_reviews_command() -> None:
    print(get_all_students())
    student_id: str = click.prompt(text="Enter Student ID", type=int)
    student: Student | None = get_student(student_id)
    if student:
        print(student.reviews)


app.cli.add_command(student_cli)
