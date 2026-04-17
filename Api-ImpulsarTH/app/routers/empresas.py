from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..dependencies import get_db
from ..models.empresa import Empresa
from ..schemas.empresa import EmpresaCreate, EmpresaResponse

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