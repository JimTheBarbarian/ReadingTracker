import uuid

from pydantic import EmailStr
from sqlalchemy import Field, Relationship, DelcarativeBase, Mapped, mapped_column, ForeignKey


class Base(DelcarativeBase):
    pass


class AuthorBase(Base):
    __tablename__ = "authors"

    id: Mapped[uuid.UUID] = mapped_column(
        primary_key=True, default=uuid.uuid4, index=True
    )
    name: Mapped[str] = mapped_column(nullable=False, index=True)

    items: Mapped[list["ItemBase"]] = Relationship(back_populates="author")

class ItemBase(Base):
    __tablename__ = "items"

    id: Mapped[uuid.UUID] = mapped_column(
        primary_key=True, default=uuid.uuid4, index=True
    )
    name: Mapped[str] = mapped_column(nullable=False, index=True)
    author: Mapped[str] = mapped_column(ForeignKey("authors.id"), nullable=False)
    




