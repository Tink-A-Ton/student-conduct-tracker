from flask import Blueprint, Response, jsonify
from ..controllers import initialize

index = Blueprint("index", __name__)


@index.route("/", methods=["GET"])
def index_page() -> str:
    return "Hello, World!"


@index.route("/init", methods=["GET"])
def init() -> Response:
    initialize()
    return jsonify(message="db initialized!")


@index.route("/health", methods=["GET"])
def health_check() -> Response:
    return jsonify({"status": "healthy"})
