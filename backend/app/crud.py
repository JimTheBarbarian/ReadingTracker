import uuid # This will generate new ids for new books/papers

from typing import Any

from sqlalchemy.orm import Session
from sqlalchemy import ForeignKey
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped, mapped_column

from app.models import Item, ItemCreate, User, UserCreate, UserUpdate

from app.core.security import get_password_hash, verify_password



def create_user(*, session: Session, user_create: UserCreate) -> User:
    db_obj = User.model_validate(
        user_create, update = {"hashed_password": get_password_hash(user_create.password)}
    )
    session.add(db_obj)

    session.commit()
    session.refresh(db_obj)
    return db_obj


def update_user(*, session: Session, db_user: User, user_in: UserUpdate) -> Any:
    

