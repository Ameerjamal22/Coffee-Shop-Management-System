from contextvars import ContextVar
from playhouse.postgres_ext import *
import peewee
from app.config.enviromentExtractor import *

db_state_default = {"closed": None, "conn": None, "ctx": None, "transactions": None}
db_state = ContextVar("db_state", default=db_state_default.copy())


class PeeweeConnectionState(peewee._ConnectionState):
    """
    creates a state for the connection to make peewee compatible with fastapi async
    """

    def __init__(self, **kwargs):
        super().__setattr__("_state", db_state)
        super().__init__(**kwargs)

    def __setattr__(self, name, value):
        self._state.get()[name] = value

    def __getattr__(self, name):
        return self._state.get()[name]

print(DATABASE_NAME)
print(DATABASE_SERVER_USERNAME)
print(DATABASE_SERVER_PASSWORD)

db = PostgresqlExtDatabase(DATABASE_NAME, user=DATABASE_SERVER_USERNAME, password=DATABASE_SERVER_PASSWORD)
db._state = PeeweeConnectionState()
