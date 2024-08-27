from typing import List
from src.utils.repository import SQLAlchemy
from src.models.task_model import TaskModel
from src.schemas.tasks_schemas import TaskAdd, Tasks, DeleteTask


class TasksRepository(SQLAlchemy):
    model = TaskModel

    def add_task(self, data: TaskAdd) -> int:
        res_id = super().add_one(data)

        return res_id


    def get_all_tasks(self) -> List[Tasks]:
        all_tasks = super().find_all()

        return all_tasks
    

    def delete_task(self, id: int) -> DeleteTask:
        res = super().delete_one(id)

        return res
    