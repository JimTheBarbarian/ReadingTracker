import uuid # This will generate new ids for new books/papers

from typing import Any

from sqlalchemy.orm import Session
from sqlalchemy import ForeignKey
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped, mapped_column





def create_user(*, session: Session)