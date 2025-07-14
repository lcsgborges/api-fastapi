from models import Admin
from sqlalchemy.orm import Session
from password_bcrypt import bcrypt_context

async def auth_admin(email:str, senha:str, session:Session):
    
    admin = session.query(Admin).filter(Admin.email == email).first()
    
    if not admin:
        return False
    
    elif not bcrypt_context.verify(senha, admin.senha):
        return False
    
    return admin