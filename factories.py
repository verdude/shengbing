from factory import Faker, SubFactory
from factory.alchemy import SQLAlchemyModelFactory
from sqlalchemy.orm import sessionmaker

from models import Caca, ErZi, ShengBing, engine

Session = sessionmaker(bind=engine)
session = Session()


class SAMeta:
    sqlalchemy_session = session
    sqlalchemy_session_persistence = "commit"


# root account
class ErZiFactory(SQLAlchemyModelFactory):
    class Meta(SAMeta):
        model = ErZi

    name = Faker("name")
    shengbing_id = None


class ShengBingFactory(SQLAlchemyModelFactory):
    class Meta(SAMeta):
        model = ShengBing

    severity = Faker("word")
    erzi = SubFactory(ErZiFactory)


class CacaFactory(SQLAlchemyModelFactory):
    class Meta(SAMeta):
        model = Caca

    description = Faker("sentence")
    shengbing = SubFactory(ShengBingFactory)
