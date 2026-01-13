from fastapi import FastAPI
from Item import Item

app = FastAPI()

@app.get("/")
def read_hoot():
    return {"Hello" : "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q : str | None = None): 
    return {"item_id" : item_id, "q": q}

@app.put("/items/{item_id}")
def update_item(item_id : int, item : Item):
    return {"item_name" : Item.name, "item_id" :item_id}