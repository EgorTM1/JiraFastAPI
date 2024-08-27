from typing import List
from src.utils.repository import SQLAlchemy
from src.models.user_model import Users
from src.schemas.users_schemas import UserAdd, Users as UsersSchema, DeleteUser


class UsersRepository(SQLAlchemy):
    model = Users

    
    def add_user(self, data: UserAdd) -> int:
        res = super().add_one(data)

        return res
    

    def get_all_users(self) -> List[UsersSchema]:
        result = super().find_all()

        return result
    
    def delete_user(self, id: int) -> DeleteUser:
        res = super().delete_one(id)

        return res