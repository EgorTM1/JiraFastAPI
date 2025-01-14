from sqlalchemy.orm import Mapped, mapped_column
from src.db.db import Base
from src.schemas.users_schemas import Users


class Users(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]


    def to_read_model(self) -> Users:
        users = Users(
            id=self.id,
            name=self.name
        )

        return users
