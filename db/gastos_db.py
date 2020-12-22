from typing import Dict

from pydantic import BaseModel
from datetime import datetime

class GastoInDB(BaseModel):
    username: str
    name: str
    date: datetime
    value: int


database_gastos = []


def save_gasto(gasto_in_db: GastoInDB):
    database_gastos.append(gasto_in_db)
    return gasto_in_db





