from sqlalchemy import Column, Integer, String
from ..database import Base

class Empresa(Base):
    __tablename__ = "empresas"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String)
    estado = Column(String)