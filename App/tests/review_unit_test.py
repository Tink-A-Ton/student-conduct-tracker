import logging, unittest
from ..models import Review

LOGGER: logging.Logger = logging.getLogger(__name__)


class ReviewUnitTests(unittest.TestCase):

    def test_new_review(self) -> None:
        new_review: Review = Review(
            "816035001",
            "000003001",
            "Please Seek Assistance",
            5,
            "Good performance, but needs to ask for help when confused.",
        )
        self.assertEqual(new_review.student_id, "816035001", "Student ID Mismatch")
        self.assertEqual(new_review.staff_id, "000003001", "Staff ID Mismatch")
        self.assertEqual(new_review.title, "Please Seek Assistance", "Title Mismatch")
        self.assertEqual(new_review.rating, 5, "Rating Mismatch")
        self.assertEqual(
            new_review.comment,
            "Good performance, but needs to ask for help when confused.",
            "Comment Mismatch",
        )
        self.assertIsNotNone(new_review.created_at, "Expected string but got None")

    def test_review_json(self) -> None:
        new_review: Review = Review(
            "816035001",
            "000003001",
            "Please Seek Assistance",
            5,
            "Good performance, but needs to ask for help when confused.",
        )
        review_json: dict[str, str | int] = new_review.get_json()
        self.assertEqual(review_json["student_id"], "816035001", "Student ID Mismatch")
        self.assertEqual(review_json["staff_id"], "000003001", "Staff ID Mismatch")
        self.assertEqual(
            review_json["title"], "Please Seek Assistance", "Title Mismatch"
        )
        self.assertEqual(review_json["rating"], 5, "Rating Mismatch")
        self.assertEqual(
            review_json["comment"],
            "Good performance, but needs to ask for help when confused.",
            "Comment Mismatch",
        )
        self.assertIsNotNone(review_json["created_at"], "Expected string but got None")
