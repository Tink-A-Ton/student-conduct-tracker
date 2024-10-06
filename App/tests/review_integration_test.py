from typing import Generator
from flask import Flask
from flask.testing import FlaskClient
import pytest, logging, unittest
from logging import Logger
from ..main import create_app
from ..database import db, create_db
from ..controllers import (
    create_student,
    create_review,
    get_all_reviews,
    create_staff,
    get_staff_reviews,
    get_student_reviews,
    get_review,
)
from ..models import Review

LOGGER: Logger = logging.getLogger(__name__)


@pytest.fixture(autouse=True, scope="module")
def empty_db() -> Generator[FlaskClient, logging.Logger, None]:
    app: Flask = create_app(
        {"TESTING": True, "SQLALCHEMY_DATABASE_URI": "sqlite:///test.db"}
    )
    create_db()
    yield app.test_client()
    db.drop_all()


class ReviewIntegrationTests(unittest.TestCase):
    def test_create_review(self) -> None:
        """Test that a review can be created and that the review model has the correct attributes"""
        create_staff("000005000", "password", "Alice", "Smith")
        create_student("816035003", "Bob", "Johnson", "BSc. Computer Science")
        create_review("816035003", "000005000", "Great work", 9, "Keep it up")
        review: Review | None = get_review(1)
        assert review is not None
        self.assertEqual(review.student_id, "816035003", "Student ID mismatch")
        self.assertEqual(review.staff_id, "000005000", "Staff ID mismatch")
        self.assertEqual(review.title, "Great work", "Review title mismatch")
        self.assertEqual(review.rating, 9, "Review rating mismatch")
        self.assertEqual(review.comment, "Keep it up", "Review comment mismatch")
        self.assertIsNotNone(
            review.created_at, "Review creation timestamp should not be None"
        )

    def test_get_student_reviews(self) -> None:
        """Test that reviews can be retrieved for a student"""
        create_staff("000006000", "staffpass", "David", "Jones")
        create_student("816035004", "Clara", "Brown", "MSc. Computer Science")
        create_review("816035004", "000006000", "Good job", 8, "Well done")
        reviews: list[Review] = get_student_reviews("816035004")
        self.assertGreater(
            len(reviews), 0, "Expected at least one review for the student"
        )
        review: Review = reviews[0]
        self.assertIsNotNone(review, "Expected a Review object, but got None")
        self.assertEqual(review.title, "Good job", "Review title mismatch for student")
        self.assertEqual(review.rating, 8, "Review rating mismatch for student")

    def test_get_staff_reviews(self) -> None:
        """Test that reviews can be retrieved for a staff member"""
        create_staff("000006022", "staffpass", "Brian", "Jones")
        create_student("816035040", "Jason", "Brown", "MSc. Computer Science")
        create_review("816035040", "000006022", "Rude Student", 1, "Was disappointed")
        reviews: list[Review] = get_staff_reviews("000006022")
        self.assertGreater(
            len(reviews), 0, "Expected at least one review for the staff"
        )
        review: Review = reviews[0]
        self.assertIsNotNone(review, "Expected a Review object, but got None")
        self.assertEqual(
            review.title, "Rude Student", "Review title mismatch for staff"
        )
        self.assertEqual(review.rating, 1, "Review rating mismatch for staff")

    def test_get_all_reviews(self) -> None:
        """Test that all reviews can be retrieved"""
        create_staff("000006001", "frankpass", "Frank", "Miller")
        create_student("816035009", "George", "Moore", "BSc. Engineering")
        create_review("816035009", "000006001", "Satisfactory", 7, "Good job")
        reviews: list[Review] = get_all_reviews()
        self.assertGreater(len(reviews), 0, "Expected at least one review in total")
        review: Review = reviews[-1]
        self.assertIsNotNone(review, "Expected a Review object, but got None")
        self.assertEqual(
            review.title, "Satisfactory", "Review title mismatch for all reviews"
        )
        self.assertEqual(review.rating, 7, "Review rating mismatch for all reviews")
