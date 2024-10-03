from flask_jwt_extended import create_access_token, JWTManager
from ..models import User
from ..controllers import get_user


def login_user(id: str, password: str) -> str | None:
    user: User | None = get_user(id)
    if user and user.check_password(password):
        return create_access_token(identity=user)
    return None


def setup_jwt(app) -> JWTManager:
    jwt = JWTManager(app)

    @jwt.user_identity_loader
    def user_identity_lookup(user) -> int:
        return user.id

    @jwt.user_lookup_loader
    def user_lookup_callback(_jwt_header, jwt_data) -> User | None:
        identity = jwt_data["sub"]
        return User.query.get(identity)

    return jwt
