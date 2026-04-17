from sqlalchemy import Column, Integer, String, ForeignKey
from ..database import Base

class Documento(Base):
    __tablename__ = "documentos"

    id = Column(Integer, primary_key=True)
    trabajador_id = Column(Integer, ForeignKey("trabajadores.id"))
    tipo_documento_id = Column(Integer)
    url_archivo = Column(String)