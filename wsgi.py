import sys
import click
from flask import Flask
from flask.cli import AppGroup
from flask_migrate import Migrate
import pytest
from App.database import get_migrate
from App.main import create_app
from App.controllers import initialize

app: Flask = create_app()
migrate: Migrate = get_migrate(app)
test = AppGroup("test", help="Testing commands")


@app.cli.command("init", help="Creates and initializes the database")
def init() -> None:
    initialize()
    print("database intialized")


@test.command("user", help="Run User tests")
@click.argument("type", default="all")
def user_tests_command(type) -> None:
    if type == "unit":
        sys.exit(pytest.main(["-k", "UserUnitTests"]))
    elif type == "int":
        sys.exit(pytest.main(["-k", "UserIntegrationTests"]))
    else:
        sys.exit(pytest.main(["-k", "App"]))


@test.command("student", help="Run Student tests")
@click.argument("type", default="all")
def student_tests_command(type) -> None:
    if type == "unit":
        sys.exit(pytest.main(["-k", "StudentUnitTests"]))
    elif type == "int":
        sys.exit(pytest.main(["-k", "StudentIntegrationTests"]))
    else:
        sys.exit(pytest.main(["-k", "App"]))


@test.command("review", help="Run Review tests")
@click.argument("type", default="all")
def review_tests_command(type) -> None:
    if type == "unit":
        sys.exit(pytest.main(["-k", "ReviewUnitTests"]))
    elif type == "int":
        sys.exit(pytest.main(["-k", "ReviewIntegrationTests"]))
    else:
        sys.exit(pytest.main(["-k", "App"]))


@test.command("all", help="Run all tests")
def run_all_tests() -> None:
    # No filters, will run all discovered tests allegedly
    sys.exit(pytest.main(["-k", "App"]))


app.cli.add_command(test)
