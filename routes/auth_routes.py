from fastapi import APIRouter, Depends, HTTPException
from models import Admin
from schemas import AdminSchema, LoginSchema
from dependencies import get_session
from services.password_bcrypt import bcrypt_context
from services.auth_admin import auth_admin
from sqlalchemy.orm import Session

auth_router = APIRouter(prefix="/auth", tags=["auth"])

@auth_router.post("/register")
async def register_admin(admin_schema:AdminSchema, session:Session = Depends(get_session)):
    """
    Rota padrão para cadastrar um admin
    """
    
    admin = session.query(Admin).filter(Admin.email == admin_schema.email).first()
    
    if admin:
        raise HTTPException(status_code=400, detail="ja existe um admin com esse email")

    else:
        print(admin_schema)
        
        senha_cript = bcrypt_context.hash(admin_schema.senha)
        
        admin_schema.nome = admin_schema.nome.upper()
        
        new_admin = Admin(admin_schema.nome, admin_schema.email, senha_cript)
        
        session.add(new_admin)
        session.commit()
        
        return {"message": "admin cadastrado com sucesso"}


@auth_router.post("/login")
async def login(login_schema:LoginSchema, session:Session=Depends(get_session)):
    
    admin = auth_admin(login_schema.email, login_schema.senha, session)
    
    if not admin:
        raise HTTPException(status_code=404, detail="Email ou senha incorretos!")
    else:
        ...