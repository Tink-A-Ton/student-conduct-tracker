import logging, unittest
from App.models import Review


LOGGER = logging.getLogger(__name__)

'''
   Review Unit Tests
'''
class ReviewUnitTests(unittest.TestCase):
    
    def test_new_review(self):
        new_review: Review = Review(
            "816035001", "000003001", "Please Seek Assistance", 5, 
            "Good performance, but needs to ask for help when confused."
        )
        self.assertEqual(new_review.student_id, "816035001")
        self.assertEqual(new_review.staff_id, "000003001")
        self.assertEqual(new_review.title, "Please Seek Assistance")
        self.assertEqual(new_review.rating, 5)
        self.assertEqual(new_review.comment, "Good performance, but needs to ask for help when confused.")
        self.assertIsNotNone(new_review.created_at)

        
    def test_review_json(self):
        new_review: Review = Review(
            "816035001", "000003001", "Please Seek Assistance", 5,
            "Good performance, but needs to ask for help when confused."
        )
        review_json: dict[str, str | int] = new_review.get_json()
        self.assertEqual(review_json["student_id"], "816035001")
        self.assertEqual(review_json["staff_id"], "000003001")
        self.assertEqual(review_json["title"], "Please Seek Assistance")
        self.assertEqual(review_json["rating"], 5)
        self.assertEqual(review_json["comment"], "Good performance, but needs to ask for help when confused.")
        self.assertIsNotNone(review_json["created_at"])