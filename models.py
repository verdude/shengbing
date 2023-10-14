from __future__ import annotations

from typing import Optional

from sqlalchemy import ForeignKey
from sqlalchemy.inspection import inspect
from sqlalchemy.orm import relationship
from sqlmodel import Field, Relationship, SQLModel, create_engine


class Base(SQLModel):
    __repr_exclude__ = None
    __args_memo__ = None

    def __repr_args__(self) -> list[Tuple[str, Any]]:
        cls = type(self)
        if cls.__args_memo__ is None:
            if cls.__repr_exclude__ is None:
                rels = inspect(cls).relationships.keys()
                fks = [fk.parent.name.rstrip("_id") for fk in cls.__table__.foreign_keys]
                cls.__repr_exclude__ = [k for k in rels if k in fks]
            cls.__args_memo__ = [(k, v) for k, v in super().__repr_args__() if k not in cls.__repr_exclude__]
        return cls.__args_memo__


class Caca(Base, table=True):
    __tablename__ = "cacas"
    id: Optional[int] = Field(default=None, primary_key=True, index=True)
    description: str = Field(index=True)
    shengbing_id: int = Field(default=None, foreign_key="shengbings.id")
    shengbing: ShengBing = Relationship(
        back_populates="cacas", sa_relationship_kwargs={"uselist": False}
    )


class ShengBing(Base, table=True):
    __tablename__ = "shengbings"
    id: Optional[int] = Field(default=None, primary_key=True, index=True)
    severity: str = Field(index=True)
    cacas: list[Caca] = Relationship(back_populates="shengbing")
    erzi: ErZi = Relationship(
        back_populates="shengbing", sa_relationship_kwargs={"uselist": False}
    )


class ErZi(Base, table=True):
    __tablename__ = "erzis"
    id: Optional[int] = Field(default=None, primary_key=True, index=True)
    name: str = Field(index=True)
    shengbing_id: int = Field(default=None, foreign_key="shengbings.id")
    shengbing: ShengBing = Relationship(
        back_populates="erzi", sa_relationship_kwargs={"uselist": False}
    )


engine = create_engine("sqlite:///example.db")

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("-c", "--create", action="store_true")
    args = parser.parse_args()

    if args.create:
        Base.metadata.create_all(engine)
