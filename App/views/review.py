from typing import Any, Literal
from flask import Blueprint, redirect, render_template, request, send_from_directory, jsonify
from flask.wrappers import Response
from flask_jwt_extended import jwt_required, get_jwt_identity
from App.controllers import get_all_reviews, create_review, get_reviews_by_student
from App.models.review import Review
from App.models.user import User

reviews = Blueprint('review', __name__)

reviews.route('/reviews', methods=['GET'])
@jwt_required()
def get_reviews_action() -> tuple[Response, int]:
    reviews: list[Review]  = get_all_reviews()
    reviews_json = [review.get_json() for review in reviews]
    response: Response = jsonify(reviews_json)
    return response, 200

reviews.route('/review', methods=['POST'])
@jwt_required()
def create_reviews_action() -> tuple[Response, int]:
    data: Any = request.get_json()
    student_id: str | None = data.get("student_id")
    rating: int | None = data.get("rating")
    comment: str | None = data.get("comment")
    if student_id is None or rating is None or comment is None:
        return jsonify(error="Data missing"), 401
    staff: User = get_jwt_identity()
    if not create_review(student_id, staff.id, rating, comment):
        return jsonify(error="Unauthorized or Invalid Data Provided"), 401
    return jsonify(message="Review created"), 201

reviews.route('/review/<id>', methods=['GET'])
@jwt_required()
def get_student_reviews_action(id) -> tuple[Response, int]:
    reviews: list[Review] | None = get_reviews_by_student(id)
    if reviews is None:
        return jsonify(error="Invalid Student ID"), 401
    reviews_json = [review.get_json() for review in reviews]
    response: Response = jsonify(reviews_json)
    return response, 200
    