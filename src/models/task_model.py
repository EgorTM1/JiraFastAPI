from sqlalchemy.orm import Mapped, mapped_column
from src.schemas.tasks_schemas import Tasks
from src.db.db import Base


class TaskModel(Base):
    __tablename__ = 'tasks'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    description: Mapped[str]


    def to_read_model(self) -> Tasks:
        tasks = Tasks(
            id=self.id,
            name=self.name,
            description=self.description
        )

        return tasks
    