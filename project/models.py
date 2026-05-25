from pydantic import BaseModel,Field
from typing import Optional
class Product(BaseModel):
    id: int
    name:str= Field(...,min_length=1)
    description:Optional[str]=None
    price: float=Field(...,gt=0)
    stock: int=Field(...,ge=0)
    category:str