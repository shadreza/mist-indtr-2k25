from fastapi import FastAPI, HTTPException
from models import Item
from typing import Dict

app = FastAPI()

# In-memory fake database
fake_db: Dict[int, Item] = {}


@app.get("/")
def read_root():
    return {"message": "FastAPI CRUD is running!"}


@app.get("/items/{item_id}")
def read_item(item_id: int):
    item = fake_db.get(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@app.post("/items/")
def create_item(item: Item):
    if item.id in fake_db:
        raise HTTPException(status_code=400, detail="Item ID already exists")
    fake_db[item.id] = item
    return {"message": "Item created", "item": item}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    if item_id not in fake_db:
        raise HTTPException(status_code=404, detail="Item not found")
    fake_db[item_id] = item
    return {"message": "Item updated", "item": item}


@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id not in fake_db:
        raise HTTPException(status_code=404, detail="Item not found")
    del fake_db[item_id]
    return {"message": "Item deleted"}
