from sqlalchemy.orm import Session
from app.models.documento import Documento
from app.models.tipo_documento import TipoDocumento


def documentos_faltantes(db: Session, trabajador_id: int):
    # Todos los tipos de documentos requeridos
    tipos = db.query(TipoDocumento).all()

    # Documentos que ya tiene el trabajador
    docs = db.query(Documento).filter(
        Documento.trabajador_id == trabajador_id
    ).all()

    tipos_subidos = {doc.tipo_documento_id for doc in docs}

    faltantes = [
        tipo.nombre for tipo in tipos
        if tipo.id not in tipos_subidos
    ]

    return faltantes