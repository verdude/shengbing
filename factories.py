from factory import Faker, SubFactory
from factory.alchemy import SQLAlchemyModelFactory
from sqlalchemy.orm import sessionmaker

from models import Caca, ErZi, ShengBing, engine

Session = sessionmaker(bind=engine)
session = Session()


class SAMeta:
    sqlalchemy_session = session
    sqlalchemy_session_persistence = "commit"


class ShengBingFactory(SQLAlchemyModelFactory):
    class Meta(SAMeta):
        model = ShengBing

    severity = Faker("word")


class ErZiFactory(SQLAlchemyModelFactory):
    class Meta(SAMeta):
        model = ErZi

    name = Faker("name")
    shengbing = SubFactory(ShengBingFactory)


class CacaFactory(SQLAlchemyModelFactory):
    class Meta(SAMeta):
        model = Caca

    description = Faker("sentence")
    shengbing = SubFactory(ShengBingFactory)


caca = CacaFactory()
caca.shengbing.erzi = ErZiFactory()
print(caca.shengbing.erzi.name)
print(caca.shengbing.erzi)
