from fastapi import FastAPI, Query
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str = None

# Path 파라미터를 포함한 GET 요청을 처리하는 엔드포인트
@app.get("/items/{item_id}")
async def read_item(item_id: int, name: str = Query(None), description: str = Query(None)):
    return {"item_id": item_id, "name": name, "description": description}

# Query string만 포함한 GET 요청을 처리하는 엔드포인트
@app.get("/items")
async def read_items(name: str = Query(None), description: str = Query(None)):
    return {"name": name, "description": description}

# POST 요청을 처리하는 엔드포인트
@app.post("/items/")
async def create_item(item: Item):
    return {"name": item.name, "description": item.description}
