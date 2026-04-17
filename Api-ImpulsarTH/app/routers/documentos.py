from fastapi import APIRouter, UploadFile, File, Depends
from sqlalchemy.orm import Session
import uuid

from ..dependencies import get_db
from ..models.documento import Documento
from ..services.storage_service import subir_archivo

router = APIRouter(prefix="/documentos", tags=["Documentos"])


@router.post("/upload")
async def subir_documento(
    trabajador_id: int,
    tipo_documento_id: int,
    archivo: UploadFile = File(...),
    db: Session = Depends(get_db)
):

    from ..models.trabajador import Trabajador

    trabajador = db.query(Trabajador).filter(
        Trabajador.id == trabajador_id
    ).first()

    empresa_id = trabajador.empresa_id

    nombre_archivo = f"empresa_{empresa_id}/trabajador_{trabajador_id}/{uuid.uuid4()}_{archivo.filename}"

    contenido = await archivo.read()  # 👈 FIX CLAVE

    url = subir_archivo(contenido, nombre_archivo)

    documento = Documento(
        trabajador_id=trabajador_id,
        tipo_documento_id=tipo_documento_id,
        url_archivo=url
    )

    db.add(documento)
    db.commit()
    db.refresh(documento)

    return {
        "mensaje": "Documento subido correctamente",
        "url": url
    }