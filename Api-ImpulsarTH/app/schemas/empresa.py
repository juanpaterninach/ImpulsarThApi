from pydantic import BaseModel

class EmpresaCreate(BaseModel):
    nombre: str

class EmpresaResponse(BaseModel):
    id: int
    nombre: str
    estado: str

    class Config:
        from_attributes = True