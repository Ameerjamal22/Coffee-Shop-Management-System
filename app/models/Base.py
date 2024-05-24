import peewee
from app.config.dbConfig import db


class BasePeeweeModel(peewee.Model):
    """
    Base peewee model for defining configurations and
    """
    class Meta:
        database = db
