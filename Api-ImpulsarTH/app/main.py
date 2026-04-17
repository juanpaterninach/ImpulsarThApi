# main.py
import os
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import auth

# Importa tus routers (asegúrate que las rutas sean correctas)
from app.routers import empresas, trabajadores, documentos

# Base de datos
from app.database import engine, Base

# Modelos (solo los importas para que se registren si usas Base)
from app.models import empresa, trabajador, documento, tipo_documento  # ← ok, aunque no se usen directamente aquí

import os
import uvicorn


app = FastAPI(
    title="Sistema de Gestión",
    description="API para la gestión de empresas, trabajadores y documentos.",
    version="1.0.0",
    docs_url="/docs",           # ← útil para debug
    redoc_url=None,             # opcional: quita si no lo necesitas
)

# CORS – para desarrollo está bien con "*", en producción pon dominios específicos
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],           # ¡cámbialo en prod!
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Crea tablas (solo se ejecuta una vez al iniciar)
Base.metadata.create_all(bind=engine)

# Incluye routers
print("DATABASE_URL:", os.getenv("DATABASE_URL"))
print("SUPABASE_URL:", os.getenv("SUPABASE_URL"))

app.include_router(empresas.router)
app.include_router(trabajadores.router)
app.include_router(documentos.router)
app.include_router(auth.router)


# Punto de entrada para desarrollo local (python main.py)
#if __name__ == "__main__":
    # Para local: puerto 8000 + reload
 #   uvicorn.run(
  #      "app.main:app",                 # ← importante: "main:app" si el archivo es main.py
   #     host="0.0.0.0",
    #    port=8000,
     #   reload=True,                # solo en dev
    #)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port)
