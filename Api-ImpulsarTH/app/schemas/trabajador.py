from pydantic import BaseModel
from typing import Optional
from datetime import datetime



class TrabajadorCreate(BaseModel):
    empresa_id: int
    nombre: str
    cedula: str
    activo: bool = True

class TrabajadorResponse(BaseModel):
    id: int
    empresa_id: int
    nombre: str
    cedula: str
    estado: str

    class Config:
        from_attributes = True

class TrabajadorUpdate(BaseModel):
    nombre: Optional[str] = None
    cedula: Optional[str] = None
    estado: Optional[str] = None
    empresa_id: Optional[int] = None
    fecha_creacion: Optional[datetime] = None
