from fastapi import FastAPI, status, HTTPException, Response
from pydantic import BaseModel

app = FastAPI()

todo_list = []


class Todo(BaseModel):
    id: int | None = None
    label: str


# Create todo    
@app.post("/todos")
async def create_todo(todo: Todo):
    new_todo = Todo(id=len(todo_list) + 1, label=todo.label)
    todo_list.append(new_todo)
    return new_todo

# Get todos
@app.get("/todos")
async def get_todos():
    return todo_list

# Get todo by id
@app.get("/todos/{todo_id}")
async def get_todo(todo_id: int):
    for todo in todo_list:
        if todo.id == todo_id:
            return todo

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail={
            "message": f"Todo [{todo_id}] not found",
            "code": "TODO_NOT_FOUND",
            "status_code": status.HTTP_404_NOT_FOUND
        }
    )
                
#Update todo    
@app.post("/todos")
async def update_todo(data: Todo):
    for todo in todo_list:
        if todo.id == data.id:
            todo.label = data.label
            return Response(status_code=status.HTTP_204_NO_CONTENT)    

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail={
            "message": f"Todo [{data.id}] not found"
            "code:" "TODO_NOT_FOUND",
            "status_code":  status.HTTP_404_NOT_FOUND
        }
    )

#Delete todo
@app.post("/todos/{todo_id}")
async def delete_todo(todo_id: int):
    for index, todo in enumerate(todo_list):
        if todo.id == todo.id:
            todo_list.pop(index)
            return Response(status_code=status.HTTP_204_NO_CONTENT)

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail={
            "message": f"Todo [{todo_id}] not found" ,
            "code": "TODO_NOT_FOUND",
            "status_code": status.HTTP_404_NOT_FOUND            
        }
    )

