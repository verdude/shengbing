from __future__ import annotations
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlmodel import Field, Relationship, SQLModel, create_engine


class Caca(SQLModel, table=True):
    __tablename__ = "cacas"
    id: Optional[int] = Field(default=None, primary_key=True, index=True)
    description: str = Field(index=True)
    shengbing_id: int = Field(default=None, foreign_key="shengbings.id")
    shengbing: ShengBing = Relationship(
        back_populates="cacas", sa_relationship_kwargs={"uselist": False}
    )


class ShengBing(SQLModel, table=True):
    __tablename__ = "shengbings"
    id: Optional[int] = Field(default=None, primary_key=True, index=True)
    severity: str = Field(index=True)
    cacas: list[Caca] = Relationship(back_populates="shengbing")
    erzi: ErZi = Relationship(
        back_populates="shengbing", sa_relationship_kwargs={"uselist": False}
    )


class ErZi(SQLModel, table=True):
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
