from pydantic import BaseModel
from typing import Optional, Text
from datetime import date


class AdminSchema(BaseModel):
    nome: str
    email: str
    senha: str
    
    class Config:
        from_attributes = True
        

class PizzaSchema(BaseModel):
    sabor: str
    preco: float
    
    class Config:
        from_attributes = True


class RefrigeranteSchema(BaseModel):
    nome: str
    litro: float
    preco: float
    
    class Config:
        from_attributes = True


class PedidoSchema(BaseModel):
    data: date
    valor: float
    frete: float
    pagamento: str
    id_cliente: int
    
    class Config:
        from_attributes = True
        

class ClienteSchema(BaseModel):
    nome: str
    telefone: str
    endereco: Optional[Text]
    
    class Config:
        from_attributes = True


class PedidoPizzaSchema(BaseModel):
    id_pedido: int
    id_pizza: int
    quantidade: int
    
    class Config:
        from_attributes = True
        
        
class PedidoRefrigeranteSchema(BaseModel):
    id_pedido: int
    id_refrigerante: int
    quantidade: int
    
    class Config:
        from_attributes = True