from sqlalchemy import Column, Integer, String, ForeignKey
from ..database import Base
from sqlalchemy import DateTime
from datetime import datetime

class Trabajador(Base):
    __tablename__ = "trabajadores"

    id = Column(Integer, primary_key=True, index=True)
    empresa_id = Column(Integer, ForeignKey("empresas.id"))
    nombre = Column(String)
    cedula = Column(String)
    estado = Column(String, default="activo")
    fecha_creacion = Column(DateTime, default=datetime.utcnow)
