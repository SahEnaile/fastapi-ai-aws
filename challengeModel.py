from pydantic import BaseModel

class challengeModel(BaseModel) :
    id : int
    title : str
    content : str 