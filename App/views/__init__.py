from flask.blueprints import Blueprint
from App.views.index import index
from App.views.auth import auth
from App.views.student import student
from App.views.review import review

views: list[Blueprint] = [index, auth, student, review]
