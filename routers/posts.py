from fastapi import APIRouter
import httpx

from models.JsonApiModel import JsonApiModel

router = APIRouter()

JSON_BASE_URI = "https://jsonplaceholder.typicode.com"

@router.get("/posts")
def read_all():
    return httpx.get(f"{JSON_BASE_URI}/posts").json()

@router.post("/posts")
def post_posts(payload : JsonApiModel) :
    payload_object = payload.model_dump()
    result = {
        "userID" : payload_object["id"], 
        "title" : payload_object["title"],
        "title" : payload_object["title"]
    }
    
    return httpx.post(
    f"{JSON_BASE_URI}/posts",
    json=result).json()