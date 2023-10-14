from factory import Faker, SubFactory
from factory.alchemy import SQLAlchemyModelFactory
from sqlalchemy.orm import sessionmaker

from models import Caca, ErZi, ShengBing, engine

# Assuming the same SQLAlchemy models and engine setup as before
Session = sessionmaker(bind=engine)
session = Session()


class SAMeta:
    sqlalchemy_session = session
    sqlalchemy_session_persistence = "commit"


class CacaFactory(SQLAlchemyModelFactory):
    class Meta(SAMeta):
        model = Caca

    description = Faker("sentence")
    shengbing = SubFactory("factories.ShengBingFactory")


class ShengBingFactory(SQLAlchemyModelFactory):
    class Meta(SAMeta):
        model = ShengBing

    severity = Faker("word")


class ErZiFactory(SQLAlchemyModelFactory):
    class Meta(SAMeta):
        model = ErZi

    name = Faker("name")
    shengbing = SubFactory(ShengBingFactory)


if __name__ == "__main__":
    import ipdb

    ipdb.set_trace()
