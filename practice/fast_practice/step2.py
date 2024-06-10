from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

todo_list = []


class Todo(BaseModel):
    id: int | None = None
    label: str
    
@app.get("/todos")
async def get_todos():
    return todo_list

@app.get("/todos/{todo_id}")
async def get_todo(todo_id: int):
    for todo in todo_list:
        if todo.id == todo_id:
            return todo
        
        

@app.post("/todos")
async def create_todo(todo: Todo):
    new_todo = Todo(id=len(todo_list) + 1, label=todo.label)
    todo_list.append(new_todo)
    return new_todo
    
@app.post("/todos")
async def update_todo():
    pass

@app.post("/todos/{todo_id}")
async def delete_todo():
    pass




