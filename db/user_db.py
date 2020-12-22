from typing import Dict
from pydantic import BaseModel
from typing import List

from models.gasto_models import Gasto
from typing import Optional

class UserInDB(BaseModel):
    username: str
    password: str
    gasto: Optional[List[Gasto]] = None
    email: str


database_users = Dict[str, UserInDB]

database_users = {
    "camilo24": UserInDB(**{"username": "camilo24",
                            "password": "root",
                            "gasto": [{"username": "camilo24",
                                       "name": "arriendo",
                                       "date": "2016-09-08 00:00:00",
                                       "value": "90000"}],
                            "email": "gaturroxd@gmail.com"}),

    "andres18": UserInDB(**{"username": "andres18",
                            "password": "root",
                            "gasto": [{"username": "andres18",
                                       "name": "arriendo",
                                       "date": "2016-09-08 00:00:00",
                                       "value": "90000"},
                                      {"username": "andres18",
                                       "name": "comida",
                                       "date": "2016-09-08 00:00:00",
                                       "value": "90000"}],
                            "email": "pacho@gmail.com"})
}


def get_user(username: str):
    if username in database_users.keys():
        return database_users[username]
    else:
        return None


def update_user(user_in_db: UserInDB):
    database_users[user_in_db.username] = user_in_db
    return user_in_db




