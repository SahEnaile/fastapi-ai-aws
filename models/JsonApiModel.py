import array

from pydantic import BaseModel

class JsonApiModel (BaseModel) :
    id : int
    title : str
    body :  str
    