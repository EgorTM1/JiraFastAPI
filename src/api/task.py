from typing import List
from fastapi import APIRouter
from src.services.tasks_repository import TasksRepository
from src.schemas.tasks_schemas import TaskAdd, Tasks, DeleteTask


router_task = APIRouter(
    prefix='/tasks',
    tags=['Tasks']
)

@router_task.get('')
def get_tasks() -> List[Tasks]:
    res = TasksRepository().get_all_tasks()

    return res


@router_task.post('')
def add_task(data: TaskAdd) -> int:
    result = TasksRepository().add_task(data)

    return result


@router_task.delete('')
def delete_task(id: int) -> DeleteTask:
    result = TasksRepository().delete_task(id)

    return result
