from fastapi import APIRouter, Depends
from models import Pedido, Refrigerante, Pizza
from schemas import PedidoSchema, PedidoPizzaSchema, PedidoRefrigeranteSchema, RefrigeranteSchema, PizzaSchema
from sqlalchemy.orm import Session
from dependencies import get_session


order_router = APIRouter(prefix="/order", tags=["order"])

@order_router.post("/register/soda")
async def register_soda(refrigerante_schema:RefrigeranteSchema):
    ...


@order_router.post("/")
async def register_order(
    pedido_schema:PedidoSchema, 
    pedido_pizza_schema: PedidoPizzaSchema, 
    pedido_refrigerante_schema:PedidoRefrigeranteSchema, 
    session:Session=Depends(get_session)):
    
    ...