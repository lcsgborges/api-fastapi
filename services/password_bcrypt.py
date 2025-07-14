from dotenv import load_dotenv

import os

from passlib.context import CryptContext

load_dotenv()

SECRET_KEY=os.getenv("SECRET_KEY")

# Criando bcryptContext
bcrypt_context = CryptContext(schemes=["bcrypt"])