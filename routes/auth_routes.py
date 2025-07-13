from fastapi import APIRouter

auth_router = APIRouter(prefix="/auth", tags=["auth"])

@auth_router.get("/login")
async def login():
    """
    Rota padrão para realizar login
    """
    ...
    
@auth_router.get("/register")
async def sign_up():
    """
    
    """