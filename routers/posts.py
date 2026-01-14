from fastapi import APIRouter, HTTPException
import httpx

from models.JsonApiModel import JsonApiModel

router = APIRouter()

JSON_BASE_URI = "https://jsonplaceholder.typicode.com"


@router.get("/posts")
def read_all():
    try:
        response = httpx.get(f"{JSON_BASE_URI}/posts")

        response.raise_for_status()

        return response.json()

    except httpx.HTTPError:
        raise HTTPException(
            status_code=500,
            detail="Error while fetching posts"
        )

@router.post("/posts")
def post_posts(payload: JsonApiModel):
    try:
        payload_object = payload.model_dump()

        result = {
            "userId": payload_object["id"],
            "title": payload_object["title"],
            "body": payload_object["body"]
        }

        response = httpx.post(
            f"{JSON_BASE_URI}/posts",
            json=result
        )

        response.raise_for_status()

        return response.json()

    except httpx.HTTPError:
        raise HTTPException(
            status_code=500,
            detail="Error while creating post"
        )