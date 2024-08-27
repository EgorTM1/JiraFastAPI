from pydantic import BaseModel, Field


class TaskAdd(BaseModel):
    name: str
    description: str = Field(max_length=30)

class Tasks(BaseModel):
    id: int
    name: str
    description: str = Field(max_length=30)

class DeleteTask(BaseModel):
    message: str
    