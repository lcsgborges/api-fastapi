from fastapi import APIRouter, Depends

customer_router = APIRouter(prefix="/customer", tags=["customers"])

@customer_router.post("/register")
async def register_customer():
    ...