from fastapi import FastAPI

import uvicorn

from dotenv import load_dotenv

import os



# Carregando variáveis de ambiente:
load_dotenv()

PORT = int(os.getenv("PORT"))

# Criando uma instancia do FastAPI:
app = FastAPI()

from routes.auth_routes import auth_router
from routes.order_routes import order_router

app.include_router(auth_router)
app.include_router(order_router)

if __name__ == '__main__':
    uvicorn.run(app, port=PORT)