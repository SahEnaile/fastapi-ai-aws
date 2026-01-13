from fastapi import FastAPI
from Item import Item
from challengeModel import challengeModel

app = FastAPI()

@app.get("/")
def read_hoot():
    return {"Hello" : "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q : str | None = None): 
    return {"item_id" : item_id, "q": q}

@app.put("/items/{item_id}")
def update_item(item_id : int, item : Item):
    return {"item_name" : item.name, "item_id" :item_id}

# ============================================================
# MINI CHALLENGE — FASTAPI FIRST STEPS
# ============================================================
#
# Create a small AI document API.
#
# A document contains:
# - id
# - title
# - content
#
# REQUIREMENTS:
#
# GET /documents
# Returns all documents.
#
# GET /documents/{document_id}
# Returns the received document ID.
#
# POST /documents
# Receives a document and returns the received data.
#
# DELETE /documents/{document_id}
# Returns a message indicating which document was removed.
#
# RULES:
# - document_id must be an int.
# - Create a Document model.
# - Document must contain title and content.
# - Use FastAPI, BaseModel, Path Parameters and Type Hints.
# - No database is required.
#
# BONUS:
# PATCH /documents/{document_id}
# Allow partial updates: title OR content.
# ============================================================
documents = []

@app.get("/documents")
def read_document():
    return{
        "Documents" : 
         documents
    }
    
@app.get("/documents/{document_id}")
def read_one_document(document_id : int) :
    return{
        "document_id" :
        document_id
    }
    
@app.post("/documents")
def post_document(payload :challengeModel) :
    
    documents.append(payload)
    
    return{
        "document" :
        payload
    }
 
@app.post("/items/")
async def create_item(item: Item):
    item_dict = item.model_dump() #transforma uma model em dict
    if item.tax is not None:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict   
    
@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item, q: str | None = None):
    result = {"item_id": item_id, **item.model_dump()} # com ** desempacota o dict para a model novamente
    if q:
        result.update({"q": q})
    return result