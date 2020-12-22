from pydantic import BaseModel
from datetime import datetime

class Gasto(BaseModel):
    username: str
    name: str
    date: datetime
    value: int
