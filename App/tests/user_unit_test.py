import logging, unittest
from App.models import User, Staff, Admin


LOGGER = logging.getLogger(__name__)

'''
   User Unit Tests
'''
class UserUnitTests(unittest.TestCase):

    def test_new_user(self):
        new_user: User = User("816030000", "pass")
        assert new_user.id == "816030000"
    
    def test_hashed_password(self):
        new_user: User = User("816030000", "pass")
        assert new_user.password != "pass"

    def test_check_password(self):
        new_user: User = User("816030000", "pass")
        assert new_user.check_password("pass")
        
    def test_user_get_json(self):
        new_user: User = User("816030000", "pass")
        user_json: dict[str, str] = new_user.get_json()
        self.assertDictEqual(user_json, {"id":"816030000"})
        
    def test_new_staff(self):
        new_staff: Staff = Staff("000003001", "pass", "Bob", "Ross")
        self.assertEqual(new_staff.id, "000003001")
        self.assertEqual(new_staff.first_name, "Bob")
        self.assertEqual(new_staff.last_name, "Ross")

        
    def test_staff_get_json(self):
        new_staff: Staff = Staff("000003001", "pass", "Bob", "Ross")
        staff_json: dict[str, str] = new_staff.get_json()
        self.assertDictEqual(staff_json, {
            "id":"000003001",
            "first_name":"Bob",
            "last_name":"Ross"
        })
        
    def test_new_admin(self):
        new_admin: Admin = Admin("000000811", "pass")
        assert new_admin.id == "000000811"