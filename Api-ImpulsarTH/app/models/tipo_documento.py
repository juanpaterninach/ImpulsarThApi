from sqlalchemy import Column, Integer, String
from ..database import Base

class TipoDocumento(Base):
    __tablename__ = "tipos_documentos"

    id = Column(Integer, primary_key=True)
    nombre = Column(String)