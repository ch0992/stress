from pydantic import BaseModel
from sqlmodel import Session
from models.todo import Todo


class CreateTodoRequest(BaseModel):
    label: str


class TodoService:
    def __init__(self, session: Session):
        self.session = session

    async def create_todo(self, data: CreateTodoRequest):
        new_todo = Todo(label=data.label)

        self.session.add(new_todo)
        await self.session.commit()

        return new_todo