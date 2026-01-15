from typing import Annotated

import httpx
from fastapi import APIRouter, Depends, HTTPException

from clients.ProductClient import ProductClient
from services.ProductServices import ProductService
from models.ProductResponse import ProductResponse

router = APIRouter()

@router.get("/products")
def get_all_products(
    client: Annotated[ProductClient, Depends(ProductClient)],
    service: Annotated[ProductService, Depends(ProductService)]
):
    try:
        data = client.get_all_products()

        return service.get_available_products(data)

    except httpx.HTTPError as error:
        raise HTTPException(
            status_code=500,
            detail="Error while fetching products"
        ) from error