from typing import List
from fastapi import APIRouter
from src.schemas.users_schemas import Users, UserAdd, DeleteUser
from src.services.users_repository import UsersRepository


router_user = APIRouter(
    prefix='/users',
    tags=['Users']
)

@router_user.get('')
def get_users() -> List[Users]:
    result = UsersRepository().get_all_users()

    return result


@router_user.post('')
def add_user(data: UserAdd) -> int:
    result = UsersRepository().add_user(data)

    return result


@router_user.delete('')
def delele_user(id: int) -> DeleteUser:
    result = UsersRepository().delete_user(id)

    return result
