from typing import Generator
from flask import Flask
from flask.testing import FlaskClient
import pytest, logging, unittest
from App.main import create_app
from App.database import db, create_db
from ..controllers import (
    create_student,
    get_all_students,
    get_student,
    get_students_by_name,
)
from ..models import Student

LOGGER: logging.Logger = logging.getLogger(__name__)


@pytest.fixture(autouse=True, scope="module")
def empty_db() -> Generator[FlaskClient, logging.Logger, None]:
    app: Flask = create_app(
        {"TESTING": True, "SQLALCHEMY_DATABASE_URI": "sqlite:///test.db"}
    )
    create_db()
    yield app.test_client()
    db.drop_all()


class StudentIntegrationTests(unittest.TestCase):
    def setUp(self) -> None:
        """Set up initial conditions for each test."""
        self.student_id = "816034793"
        self.first_name = "Fabian"
        self.last_name = "Ruiz"
        self.programme = "BSc. Sociology"
        self.student_data: dict[str, str] = {
            "id": self.student_id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "programme": self.programme,
        }

    def test_create_student(self) -> None:
        """Test creating a student and verifying the details."""
        create_student(self.student_id, self.first_name, self.last_name, self.programme)
        student: Student | None = get_student(self.student_id)
        self.assertIsNotNone(
            student, "Expected to retrieve a Student object, but got None"
        )
        assert student is not None
        self.assertEqual(student.id, self.student_id, "Student ID mismatch")
        self.assertEqual(student.first_name, self.first_name, "First name mismatch")
        self.assertEqual(student.last_name, self.last_name, "Last name mismatch")
        self.assertEqual(student.programme, self.programme, "Program mismatch")

    def test_get_students_by_name(self) -> None:
        """Test fetching students by their name."""
        create_student("816033893", "Jane", "Doe", "BSc. Mathematics")
        students: list[Student] = get_students_by_name("Jane", "Doe")
        self.assertEqual(len(students), 1, "Expected to find exactly one student")
        student: Student = students[0]
        self.assertEqual(student.first_name, "Jane", "First name mismatch")
        self.assertEqual(student.last_name, "Doe", "Last name mismatch")
        self.assertEqual(student.programme, "BSc. Mathematics", "Programme mismatch")

    def test_get_all_students(self) -> None:
        """Test fetching all students."""
        create_student("816034893", "Ruben", "Diaz", "MSc. Computer Science")
        students: list[Student] = get_all_students()
        self.assertGreater(
            len(students), 0, "Expected at least one student in the database"
        )
        student_ids: list[str] = [student.id for student in students]
        self.assertIn(
            "816034893",
            student_ids,
            "Expected student ID to be in the list of all students",
        )
