# app/schemas/usuario.py
from pydantic import BaseModel
from pydantic import BaseModel

class UsuarioCreate(BaseModel):
    email: str
    password: str

class UsuarioLogin(BaseModel):
    email: str
    password: str

class UsuarioResponse(BaseModel):
    id: int
    email: str

    class Config:
        from_attributes = True


class UsuarioCreate(BaseModel):
    email: str
    password: str
    rol: str  # 👈 agregar esto