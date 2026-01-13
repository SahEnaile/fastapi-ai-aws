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
    return {"item_name" : Item.name, "item_id" :item_id}

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

@app.get("/documents")
def read_document():
    return{
        "Documents" : 
        challengeModel
    }
    
@app.get("/documents/{document_id}")
def read_one_document(document_id : int) :
    return{
        "document_id" :
        challengeModel.id
    }
    
@app.post("/documents")
def post_document(payload :challengeModel) :
    return{
        "document" :
        challengeModel
    }