from database import SessionLocal
from werkzeug.security import check_password_hash
from models import Usuario

def verificar_usuario(email_usuario, senha_usuario):
    db = SessionLocal()
    try:
        usuario = db.query(Usuario).filter(
            Usuario.email == email_usuario
        ).first()

        if usuario and check_password_hash(usuario.senha, senha_usuario):
            return usuario
        
        return None

    finally:
        db.close()