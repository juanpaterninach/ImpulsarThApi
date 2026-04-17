from sqlalchemy import Column, Integer, String, ForeignKey
from ..database import Base

class Trabajador(Base):
    __tablename__ = "trabajadores"

    id = Column(Integer, primary_key=True, index=True)
    empresa_id = Column(Integer, ForeignKey("empresas.id"))
    nombre = Column(String)
    cedula = Column(String)
    estado = Column(String, default="activo")