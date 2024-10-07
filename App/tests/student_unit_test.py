import logging, unittest
from ..models import Student

LOGGER: logging.Logger = logging.getLogger(__name__)


class StudentUnitTests(unittest.TestCase):
    def test_new_student(self) -> None:
        new_student: Student = Student(
            "816035001", "Ruben", "Dias", "BSc. Computer Science (Special)"
        )
        self.assertEqual(new_student.id, "816035001", "Student ID Mismatch")
        self.assertEqual(new_student.first_name, "Ruben", "First Name Mismatch")
        self.assertEqual(new_student.last_name, "Dias", "Last Name Mismatch")
        self.assertEqual(
            new_student.programme,
            "BSc. Computer Science (Special)",
            "Programme Mismatch",
        )

    def test_student_get_json(self) -> None:
        new_student: Student = Student(
            "816035001", "Ruben", "Dias", "BSc. Computer Science (Special)"
        )
        student_json: dict[str, str] = new_student.get_json()
        self.assertDictEqual(
            student_json,
            {
                "id": "816035001",
                "first_name": "Ruben",
                "last_name": "Dias",
                "programme": "BSc. Computer Science (Special)",
            },
            "Student JSON object does not match expected fields or values",
        )
