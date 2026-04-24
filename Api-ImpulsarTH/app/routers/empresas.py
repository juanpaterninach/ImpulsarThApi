from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..dependencies import get_db
from ..models.empresa import Empresa
from ..schemas.empresa import EmpresaCreate, EmpresaResponse
from fastapi import HTTPException

router = APIRouter(prefix="/empresas", tags=["Empresas"])


@router.post("/", response_model=EmpresaResponse)
def crear_empresa(empresa: EmpresaCreate, db: Session = Depends(get_db)):
    nueva_empresa = Empresa(
        nombre=empresa.nombre,
        estado="activa"
    )

    db.add(nueva_empresa)
    db.commit()
    db.refresh(nueva_empresa)

    return nueva_empresa


@router.get("/", response_model=list[EmpresaResponse])
def listar_empresas(db: Session = Depends(get_db)):
    return db.query(Empresa).all()

@router.patch("/{empresa_id}/estado")
def cambiar_estado_empresa(
    empresa_id: int,
    estado: str,
    db: Session = Depends(get_db)
):
    empresa = db.query(Empresa).filter(
        Empresa.id == empresa_id
    ).first()

    if not empresa:
        raise HTTPException(status_code=404, detail="Empresa no encontrada")

    if estado not in ["activa", "inactiva"]:
        raise HTTPException(status_code=400, detail="Estado inválido")

    empresa.estado = estado

    db.commit()

    return {"mensaje": f"Empresa {estado}"}
