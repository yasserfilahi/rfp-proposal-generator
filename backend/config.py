import os
from dotenv import load_dotenv
from pathlib import Path
from supabase import create_client, Client # On importe les outils pour Supabase

# On supprime les imports de pymongo et certifi car ils ne sont plus utilisés
# from pymongo import MongoClient
# import certifi

load_dotenv()

class Config:
    # Flask
    DEBUG = os.getenv("DEBUG", "false").lower() == "true"
    SECRET_KEY = os.getenv("APP_SECRET", "change-this")
    TMP_DIR = Path("./tmp")
    TMP_FILE_PATH = str(TMP_DIR / "upload.tmp")
    
    # Supabase - Ces variables sont maintenant les plus importantes
    SUPABASE_URL = os.getenv("SUPABASE_URL")
    SUPABASE_KEY = os.getenv("SUPABASE_KEY")

    # On vérifie que les variables Supabase existent, sinon l'application ne peut pas fonctionner
    if not SUPABASE_URL or not SUPABASE_KEY:
        raise RuntimeError("SUPABASE_URL ou SUPABASE_KEY manquant dans .env")

    # On crée le client Supabase qui sera utilisé par le reste de l'application
    SUPABASE_CLIENT: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

    # SMTP
    SMTP_HOST = os.getenv("SMTP_HOST", "smtp.gmail.com")
    SMTP_PORT = int(os.getenv("SMTP_PORT", "587"))
    SMTP_USER = os.getenv("SMTP_USER")
    SMTP_PASS = os.getenv("SMTP_PASS")

    # OTP
    OTP_PEPPER = os.getenv("OTP_PEPPER", "change-me")
    OTP_TTL_SEC = int(os.getenv("OTP_TTL_SEC", "600"))
    RESEND_INTERVAL_SEC = int(os.getenv("RESEND_INTERVAL_SEC", "60"))
    REG_TOKEN_TTL_MIN = int(os.getenv("REG_TOKEN_TTL_MIN", "15"))
    
    # Weaviate
    WEAVIATE_HOST = os.getenv("WEAVIATE_HOST", "localhost")
    WEAVIATE_HTTP_PORT = int(os.getenv("WEAVIATE_HTTP_PORT", "8080"))
    WEAVIATE_GRPC_PORT = int(os.getenv("WEAVIATE_GRPC_PORT", "50051"))
    
    # Chunking + modèle
    EMBED_MODEL     = os.getenv("EMBED_MODEL", "intfloat/multilingual-e5-small")
    CHUNK_MAX_CHARS      = int(os.getenv("CHUNK_MAX_CHARS", "1200"))
    CHUNK_OVERLAP  = int(os.getenv("CHUNK_OVERLAP", "200"))

    HYBRID_ALPHA = 0.5
    SEARCH_TOP_K = 1

    api_key = "AIzaSyDqV770pDFn5z_seVND3S20C0d_TNhYtH8"

    # Le bloc MongoDB a été entièrement supprimé.
