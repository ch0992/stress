from fastapi import FastAPI

app = FastAPI()

todo_list = []
    
@app.get("/todos")
async def get_todos():
    pass

@app.get("/todos/{todo_id}")
async def get_todo():
    pass    
    
@app.post("/todos")
async def create_todo():
    pass

@app.post("/todos")
async def update_todo():
    pass

@app.post("/todos/{todo_id}")
async def delete_todo():
    pass




