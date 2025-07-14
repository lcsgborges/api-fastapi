from pydantic import BaseModel
from typing import Optional, Text


class AdminSchema(BaseModel):
    nome: str
    email: str
    senha: str
    
    class Config:
        from_attributes = True