from flask import Blueprint, request, jsonify
from flask.wrappers import Response
from flask_jwt_extended import jwt_required, get_jwt_identity
from App.controllers import get_all_reviews, create_review, get_student_reviews
from App.models import Review, User

review = Blueprint("review", __name__)


@review.route("/reviews", methods=["GET"])
@jwt_required()
def get_reviews() -> tuple[Response, int]:
    reviews: list[Review] = get_all_reviews()
    return jsonify([r.get_json() for r in reviews]), 200


@review.route("/reviews/<student_id>", methods=["GET"])
@jwt_required()
def search_student_reviews(student_id) -> tuple[Response, int]:
    reviews: list[Review] = get_student_reviews(student_id)
    if reviews is None:
        return jsonify(error="Reviews not found"), 404
    return jsonify(r.get_json() for r in reviews), 200


@review.route("/review", methods=["POST"])
@jwt_required()
def create_reviews_action() -> tuple[Response, int]:
    data = request.get_json()
    student_id: str | None = data.get("student_id")
    rating: int | None = data.get("rating")
    comment: str | None = data.get("comment")
    if student_id is None or rating is None or comment is None:
        return jsonify(error="Data missing"), 401
    staff: User = get_jwt_identity()
    if not create_review(student_id, staff.id, rating, comment):
        return jsonify(error="Unauthorized or Invalid Data Provided"), 401
    return jsonify(message="Review created"), 201
