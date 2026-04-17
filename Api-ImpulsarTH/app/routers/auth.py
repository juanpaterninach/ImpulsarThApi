from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.dependencies import get_db
from app.models.usuario import Usuario
from app.schemas.usuario import UsuarioCreate, UsuarioLogin
from app.utils.security import hash_password, verify_password, create_token

router = APIRouter(prefix="/auth", tags=["Auth"])


# ✅ REGISTRO
@router.post("/register")
def register(user: UsuarioCreate, db: Session = Depends(get_db)):

    existe = db.query(Usuario).filter(Usuario.email == user.email).first()

    if existe:
        raise HTTPException(status_code=400, detail="Usuario ya existe")

    nuevo = Usuario(
        email=user.email,
        password_hash=hash_password(user.password),
        rol=user.rol# 👈 FIX AQUÍ
        
    )

    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)

    return {"msg": "Usuario creado"}


# ✅ LOGIN
@router.post("/login")
def login(user: UsuarioLogin, db: Session = Depends(get_db)):

    db_user = db.query(Usuario).filter(Usuario.email == user.email).first()

    if not db_user:
        raise HTTPException(status_code=400, detail="Credenciales inválidas")

    if not verify_password(user.password, db_user.password_hash):
        raise HTTPException(status_code=400, detail="Credenciales inválidas")

    token = create_token({"sub": db_user.email})

    return {
        "access_token": token,
        "token_type": "bearer"
    }