from argparse import ArgumentParser

from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Caca(Base):
    __tablename__ = "cacas"
    id = Column(Integer, primary_key=True)
    description = Column(String, index=True)
    shengbing_id = Column(Integer, ForeignKey("shengbings.id"))
    shengbing = relationship("ShengBing", back_populates="cacas")


class ShengBing(Base):
    __tablename__ = "shengbings"
    id = Column(Integer, primary_key=True)
    severity = Column(String, index=True)
    cacas = relationship("Caca", back_populates="shengbing")
    erzi = relationship("ErZi", uselist=False, back_populates="shengbing")


class ErZi(Base):
    __tablename__ = "erzis"
    id = Column(Integer, primary_key=True)
    name = Column(String, index=True)
    shengbing_id = Column(Integer, ForeignKey("shengbings.id"))
    shengbing = relationship("ShengBing", back_populates="erzi", uselist=False)


engine = create_engine("sqlite:///example.db")

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("-c", "--create", action="store_true")
    args = parser.parse_args()

    if args.create:
        Base.metadata.create_all(engine)
