from .user import User


class Admin(User):
    __mapper_args__: dict[str, str] = {"polymorphic_identity": "admin"}

    def __init__(self, id: str, password: str) -> None:
        super().__init__(id, password)
