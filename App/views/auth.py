from flask import Blueprint, Response, jsonify, request
from flask_jwt_extended import jwt_required, set_access_cookies, unset_jwt_cookies
from ..controllers.auth import login_user

auth = Blueprint("auth", __name__)


@auth.route("/login", methods=["POST"])
def login() -> tuple[Response, int]:
    data = request.get_json()
    id: str | None = data.get("id")
    password: str | None = data.get("password")
    if id is None or password is None:
        return jsonify(error="Data missing"), 400
    token: str | None = login_user(id, password)
    if token is None:
        return jsonify(error="Invalid credentials"), 401
    response: Response = jsonify(login=True)
    set_access_cookies(response, token)
    return response, 200


@auth.route("/logout", methods=["POST"])
@jwt_required()
def logout() -> tuple[Response, int]:
    response: Response = jsonify(logout=True)
    unset_jwt_cookies(response)
    return response, 200
