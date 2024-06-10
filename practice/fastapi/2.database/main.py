from fastapi import FastAPI
from database import init_db

app = FastAPI()

@app.on_event("startup")
async def on_startup():
    await init_db()

@app.post("/todos", response_model=Todo)
async def create_todo(*, data: CreateTodoRequest, todo_service: TodoService = Depends(get_todo_service)):
    new_todo = await todo_service.create_todo(data)

    return new_todo