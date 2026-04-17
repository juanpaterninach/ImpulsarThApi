from supabase import create_client
import os

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)


def subir_archivo(contenido, nombre_archivo):

    #contenido = file.read()

    supabase.storage.from_("documentos").upload(
        nombre_archivo,
        contenido,
        {"content-type": "application/pdf"}  # 👈 agregado
    )

    url = f"{SUPABASE_URL}/storage/v1/object/public/documentos/{nombre_archivo}"

    return url