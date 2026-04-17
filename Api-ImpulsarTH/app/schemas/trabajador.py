from pydantic import BaseModel


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