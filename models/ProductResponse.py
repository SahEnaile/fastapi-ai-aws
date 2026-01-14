from pydantic import BaseModel

class ProductResponse (BaseModel):
    id : int
    title: str
    description: str
    category: str
    price: float