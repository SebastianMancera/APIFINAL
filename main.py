from typing import List

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime

from db.gastos_db import GastoInDB, save_gasto
from db.user_db import update_user, database_users, UserInDB
from fastapi.encoders import jsonable_encoder

from fastapi.middleware.cors import CORSMiddleware

from db.user_db import get_user
from models.gasto_models import Gasto
from models.user_models import UserOut

api = FastAPI()

origins = [
    "http://localhost.tiangolo.com", "https://localhost.tiangolo.com",
    "http://localhost", "http://localhost:8080",
    "https://cajero-app16.herokuapp.com"
]

api.add_middleware(
    CORSMiddleware, allow_origins=origins,
    allow_credentials=True, allow_methods=["*"], allow_headers=["*"],
)


@api.get("/user/gastos/{username}")
async def get_gastos(username: str):
    user_in_db = get_user(username)
    if user_in_db == None:
        raise HTTPException(status_code=404, detail="El usuario no existe")
    user_out = UserOut(**user_in_db.dict())
    return user_out

@api.put("/user/gastos/crearGasto")
async def create_gasto(gasto_in_db: Gasto):
    user_in_db = get_user(gasto_in_db.username)
    if user_in_db == None:
        raise HTTPException(status_code=404, detail="El usuario no existe")
    gasto_in_db = GastoInDB(**gasto_in_db.dict())
    gasto_in_db = save_gasto(gasto_in_db)
    gasto = Gasto(**gasto_in_db.dict())
    return gasto


"""
@api.post("/user/gastos/{username}")
async def crear_gasto(username: str):
    user_in_db = get_user(username)
    if user_in_db == None:
        raise HTTPException(status_code=404, detail="El usuario no existe")
    user_out = UserOut(**user_in_db.gasto[])
    return {"Gasto Creado": True}

"""

@api.post("/user/gastos/{username}")
async def crear_usuario(usuario : UserInDB):
    if usuario.username in database_users:
        raise HTTPException(status_code=404, detail="El usuario ya existe")
    else:
        database_users[usuario.username] = usuario
        return {"Usuario Creado": True}
"""
@api.delete("/user/gastos/{username}")
async def eliminar_usuario(username: str):
    user_in_db = get_user(username)
    if user_in_db == None:
        raise HTTPException(status_code=404, detail="El usuario no existe")
    else:
        del database_users[user_in_db]
        return {"Usuario Eliminado": True}
"""

@api.get("/user/usuarios/{username}")
async def obtener_email(username: str):
    user_in_db = get_user(username)
    if user_in_db == None:
        raise HTTPException(status_code=404, detail="El usuario no existe")
    else:
        return user_in_db.email
