from flask import Flask
from flask_migrate import Migrate
from App.database import get_migrate
from App.main import create_app
from App.controllers import initialize

app: Flask = create_app()
migrate: Migrate = get_migrate(app)


@app.cli.command("init", help="Creates and initializes the database")
def init() -> None:
    initialize()
    print("database intialized")
