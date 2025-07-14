from fastapi import APIRouter, Depends, HTTPException
from models import Admin
from schemas import AdminSchema, LoginSchema, DeleteAdminSchema
from dependencies import get_session
from services.password_bcrypt import bcrypt_context
from services.auth_admin import auth_admin
from sqlalchemy.orm import Session

auth_router = APIRouter(prefix="/auth", tags=["auth"])

@auth_router.post("/register")
async def register_admin(admin_schema:AdminSchema, session:Session = Depends(get_session)):
    """
    Rota para cadastrar um novo admin
    """
    
    admin = session.query(Admin).filter(Admin.email == admin_schema.email).first()
    
    if admin:
        raise HTTPException(status_code=400, detail="Já existe um admin com esse email")

    else:
        if admin_schema.senha != admin_schema.senha2:
            raise HTTPException(status_code=400, detail="As senhas não coincidem")
        
        senha_cript = bcrypt_context.hash(admin_schema.senha)
        
        admin_schema.nome = admin_schema.nome.upper()
        
        new_admin = Admin(admin_schema.nome, admin_schema.email, senha_cript)
        
        session.add(new_admin)
        session.commit()
        
        return {"message": "admin cadastrado com sucesso"}


@auth_router.post("/login")
async def login_admin(login_schema:LoginSchema, session:Session=Depends(get_session)):
    """
    Rota para realizar login de um admin
    """
    
    admin = await auth_admin(login_schema.email, login_schema.senha, session)
    
    if not admin:
        raise HTTPException(status_code=404, detail="Email ou senha incorretos!")
    else:
        return {'detail': 'login feito com sucesso'}
    

@auth_router.delete("/delete")
async def delete_admin(delete_admin_schema:DeleteAdminSchema, session:Session=Depends(get_session)):
    """
    Rota para deletar uma conta de admin 
    """
    
    admin = await auth_admin(delete_admin_schema.email, delete_admin_schema.senha, session)
    
    if not admin:
        raise HTTPException(status_code=404, detail="Senha incorreta!")
    
    else:
        row = session.query(Admin).filter(Admin.email== admin.email).delete(synchronize_session="fetch")
        session.commit()
        if row >= 1:
            return {"detail": "Sua conta foi excluida com sucesso!"}
        else:
            raise HTTPException(status_code=400, detail="Erro ao excluir sua conta")