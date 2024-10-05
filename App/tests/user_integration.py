from flask import Flask
from flask.testing import FlaskClient
import pytest, logging, unittest
from typing import Generator
from App.main import create_app
from App.database import db, create_db
from App.models import User
from ..controllers import (
    get_all_users,
    get_user,
    create_user,
    login_user,
    create_admin,
    is_admin,
)

LOGGER: logging.Logger = logging.getLogger(__name__)


@pytest.fixture(autouse=True, scope="module")
def empty_db() -> Generator[FlaskClient, logging.Logger, None]:
    app: Flask = create_app(
        {"TESTING": True, "SQLALCHEMY_DATABASE_URI": "sqlite:///test.db"}
    )
    create_db()
    yield app.test_client()
    db.drop_all()


class UsersIntegrationTests(unittest.TestCase):
    def setUp(self) -> None:
        """Set up initial conditions for each test."""
        self.user_id = "816035671"
        self.admin_id = "admin123"
        self.password = "password"
        self.admin_password = "adminpass"

    def test_create_user(self) -> None:
        """Test creating a user and verifying the user details."""
        create_user(self.user_id, self.password)
        user: User = get_user(self.user_id)
        self.assertIsNotNone(user, "Expected to retrieve a User object, but got None")
        self.assertEqual(user.id, self.user_id, "User ID mismatch")

    def test_login(self) -> None:
        """Test user login functionality."""
        create_user("816035661", self.password)
        token: str | None = login_user("816035661", self.password)
        self.assertIsNotNone(
            token, "Expected a token to be returned upon successful login"
        )

    def test_get_all_users(self) -> None:
        """Test fetching all users from the database."""
        create_user("816035861", self.password)
        users: list[User] = get_all_users()
        self.assertGreater(len(users), 0, "Expected at least one user in the database")
        user_ids: list[str] = [user.id for user in users]
        self.assertIn(
            "816035861",
            user_ids,
            "Expected created user ID to be in the list of all users",
        )

    def test_is_admin(self) -> None:
        """Test the functionality to check if a user is an admin."""
        create_admin(self.admin_id, self.admin_password)
        self.assertTrue(
            is_admin(self.admin_id),
            "Expected admin status to be True for created admin",
        )
