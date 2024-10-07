import sys
import click
from flask import Flask
from flask.cli import AppGroup
from flask_migrate import Migrate
import pytest
from App.database import get_migrate
from App.main import create_app
from App.controllers import initialize
from rich.console import Console
from rich.table import Table

app: Flask = create_app()
migrate: Migrate = get_migrate(app)
console = Console()
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


@test.command("user", help="Runs User tests Unit and/or Integration")
@click.argument("type", default="all")
def user_tests_command(type) -> None:
    run_tests(type, "UserUnitTests", "UserIntegrationTests")


@test.command("student", help="Runs Student tests Unit and/or Integration")
@click.argument("type", default="all")
def student_tests_command(type) -> None:
    run_tests(type, "StudentUnitTests", "StudentIntegrationTests")


@test.command("review", help="Runs Review tests Unit and/or Integration")
@click.argument("type", default="all")
def review_tests_command(type) -> None:
    run_tests(type, "ReviewUnitTests", "ReviewIntegrationTests")


@test.command("unit", help="Runs all Unit tests")
def run_all_unit_tests() -> None:
    if pytest.main(["-k", "UserUnitTests"]) == 0:
        pytest.main(["-k", "StudentUnitTests"])
    sys.exit(pytest.main(["-k", "ReviewUnitTests"]))


@test.command("int", help="Runs all Integration tests")
def run_all_integration_tests() -> None:
    if pytest.main(["-k", "UserIntegrationTests"]) == 0:
        pytest.main(["-k", "StudentIntegrationTests"])
    sys.exit(pytest.main(["-k", "ReviewIntegrationTests"]))


@test.command("all", help="Runs all tests Unit and Integration")
def run_all_tests() -> None:
    if pytest.main(["-k", "UserUnitTests"]) == 0:
        pytest.main(["-k", "UserIntegrationTests"])
    if pytest.main(["-k", "StudentUnitTests"]) == 0:
        pytest.main(["-k", "StudentIntegrationTests"])
    if pytest.main(["-k", "ReviewUnitTests"]) == 0:
        pytest.main(["-k", "ReviewIntegrationTests"])
    sys.exit(0)


@app.cli.command("help", help="Displays all available commands and their descriptions.")
def help_command() -> None:
    ctx = click.Context(app.cli)
    groups: dict[str, AppGroup] = {"test": test}
    table = Table(title="Available Commands")
    table.add_column("Command", justify="left", style="cyan", no_wrap=True)
    table.add_column("Description", justify="left", style="magenta")
    for cmd in app.cli.list_commands(ctx):
        command = app.cli.get_command(ctx, cmd)
        table.add_row(cmd, command.help if command else "No description available")
    for group_name, group in groups.items():
        for cmd in group.list_commands(ctx):
            command = group.get_command(ctx, cmd)
            table.add_row(
                f"{group_name} {cmd}",
                command.help if command else "No description available",
            )
    console.print(table)


app.cli.add_command(test)
