from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..dependencies import get_db
from ..models.trabajador import Trabajador
from ..schemas.trabajador import TrabajadorCreate, TrabajadorResponse
from ..models.documento import Documento
from app.services.trabajador_service import documentos_faltantes
from fastapi import HTTPException
from ..models.empresa import Empresa

router = APIRouter(prefix="/trabajadores", tags=["Trabajadores"])


@router.post("/", response_model=TrabajadorResponse)
def crear_trabajador(trabajador: TrabajadorCreate, db: Session = Depends(get_db)):

    # ✅ Validar empresa
    empresa = db.query(Empresa).filter(
        Empresa.id == trabajador.empresa_id
    ).first()

    if not empresa:
        raise HTTPException(status_code=400, detail="La empresa no existe")

    # ✅ Validar cédula única
    existente = db.query(Trabajador).filter(
        Trabajador.cedula == trabajador.cedula
    ).first()

    if existente:
        raise HTTPException(status_code=400, detail="La cédula ya está registrada")

    # ✅ Crear trabajador
    nuevo_trabajador = Trabajador(
        empresa_id=trabajador.empresa_id,
        nombre=trabajador.nombre,
        cedula=trabajador.cedula,
        estado="activo"
    )

    db.add(nuevo_trabajador)
    db.commit()
    db.refresh(nuevo_trabajador)

    return nuevo_trabajador


@router.get("/", response_model=list[TrabajadorResponse])
def listar_trabajadores(db: Session = Depends(get_db)):
    return db.query(Trabajador).all()

@router.get("/{trabajador_id}/documentos", summary="Listar documentos de un trabajador")
def listar_documentos_trabajador(trabajador_id: int, db: Session = Depends(get_db)):

    documentos = db.query(Documento).filter(
        Documento.trabajador_id == trabajador_id
    ).all()

    return documentos

@router.get("/{trabajador_id}/faltantes", summary="Documentos faltantes")
def obtener_documentos_faltantes(trabajador_id: int, db: Session = Depends(get_db)):

    faltantes = documentos_faltantes(db, trabajador_id)

    return {
        "trabajador_id": trabajador_id,
        "documentos_faltantes": faltantes,
        "estado": "completo" if len(faltantes) == 0 else "incompleto"
    }


@router.put("/{trabajador_id}/estado", summary="Activar o desactivar trabajador")
def cambiar_estado_trabajador(trabajador_id: int, estado: str, db: Session = Depends(get_db)):

    trabajador = db.query(Trabajador).filter(
        Trabajador.id == trabajador_id
    ).first()

    if not trabajador:
        raise HTTPException(status_code=404, detail="Trabajador no encontrado")

    if estado not in ["activo", "inactivo"]:
        raise HTTPException(status_code=400, detail="Estado inválido")

    trabajador.estado = estado
    db.commit()
    db.refresh(trabajador)

    return {
        "msg": "Estado actualizado",
        "trabajador_id": trabajador.id,
        "nuevo_estado": trabajador.estado
    }