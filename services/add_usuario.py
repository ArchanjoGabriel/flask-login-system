from database import SessionLocal
from werkzeug.security import generate_password_hash
from models import Usuario

def novo_usuario(nome_usuario, email_usuario, senha_usuario):
    
    db = SessionLocal()
    try:
        usuario_existe = db.query(Usuario).filter(
            Usuario.email == email_usuario
        ).first()

        if usuario_existe:
            return True

        hash_senha_usuario = generate_password_hash(senha_usuario)

        usuario = Usuario(
            nome=nome_usuario,
            email=email_usuario,
            senha=hash_senha_usuario
        )

        db.add(usuario)
        db.commit()
    finally:
        db.close()