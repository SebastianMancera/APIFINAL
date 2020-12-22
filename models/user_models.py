from pydantic import  BaseModel
from typing import List, Optional

from models.gasto_models import Gasto


class UserIn(BaseModel):
    username: str
    password: str

class UserOut(BaseModel):
    username: str
    gasto: Optional[List[Gasto]] = None

