from flask import Blueprint, Response, jsonify, request
from flask_jwt_extended import get_jwt_identity, jwt_required
from ..models import Student
from ..controllers import (
    create_student,
    get_all_students,
    get_student,
    get_students_by_name,
    is_admin,
)

student = Blueprint("student", __name__)


@student.route("/student/<id>", methods=["GET"])
@jwt_required()
def search_student(id: str) -> tuple[Response, int]:
    student: Student | None = get_student(id)
    if student is None:
        return jsonify(error="Student not found"), 404
    return jsonify(student.get_json()), 200


@student.route("/students", methods=["GET"])
@jwt_required()
def search_students() -> tuple[Response, int]:
    students: list[Student] = get_all_students()
    return jsonify([s.get_json() for s in students]), 200


@student.route("/students/<first_name>-<last_name>", methods=["GET"])
@jwt_required()
def search_students_by_name(first_name: str, last_name: str) -> tuple[Response, int]:
    students: list[Student] = get_students_by_name(first_name, last_name)
    if not students:
        return jsonify(error="Students not found"), 404
    return jsonify([s.get_json() for s in students]), 200


@student.route("/student", methods=["POST"])
@jwt_required()
def add_student() -> tuple[Response, int]:
    admin: bool = is_admin(get_jwt_identity())
    if not admin:
        return jsonify(error="Unauthorized"), 401
    data = request.get_json()
    if not (
        data.get("id")
        and data.get("first_name")
        and data.get("last_name")
        and data.get("programme")
    ):
        return jsonify(error="Missing required fields"), 400
    created: bool = create_student(
        data["id"], data["first_name"], data["last_name"], data["programme"]
    )
    if created:
        return jsonify(success=True), 200
    return jsonify(success=False), 400
