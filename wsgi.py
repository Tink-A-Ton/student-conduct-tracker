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
    print("database initialized")


def run_tests(test_type: str, unit_key: str, integration_key: str) -> None:
    if test_type == "unit":
        sys.exit(pytest.main(["-k", unit_key]))
    elif test_type == "int":
        sys.exit(pytest.main(["-k", integration_key]))
    else:
        unit_result: int | pytest.ExitCode = pytest.main(["-k", unit_key])
        if unit_result == 0:
            integration_result: int | pytest.ExitCode = pytest.main(
                ["-k", integration_key]
            )
            sys.exit(integration_result)
        else:
            sys.exit(unit_result)


@test.command("user", help="Run User tests")
@click.argument("type", default="all")
def user_tests_command(type) -> None:
    run_tests(type, "UserUnitTests", "UserIntegrationTests")


@test.command("student", help="Run Student tests")
@click.argument("type", default="all")
def student_tests_command(type) -> None:
    run_tests(type, "StudentUnitTests", "StudentIntegrationTests")


@test.command("review", help="Run Review tests")
@click.argument("type", default="all")
def review_tests_command(type) -> None:
    run_tests(type, "ReviewUnitTests", "ReviewIntegrationTests")


@test.command("all", help="Run all tests")
def run_all_tests() -> None:
    if pytest.main(["-k", "UserUnitTests"]) == 0:
        pytest.main(["-k", "UserIntegrationTests"])
    if pytest.main(["-k", "StudentUnitTests"]) == 0:
        pytest.main(["-k", "StudentIntegrationTests"])
    if pytest.main(["-k", "ReviewUnitTests"]) == 0:
        pytest.main(["-k", "ReviewIntegrationTests"])
    sys.exit(0)


app.cli.add_command(test)
