from sqlalchemy import create_engine, Column, Integer, Float, String, Text, ForeignKey, Date
from sqlalchemy.orm import declarative_base
from sqlalchemy.schema import PrimaryKeyConstraint

# comandos alembic:
# alembic init alembic
# migracao: alembic revision --autogenerate -m "<message>"
# subir o banco: alembic upgrade head

# conexão com o DB
db = create_engine("sqlite:///database/banco.db")

# base do banco de dados 
Base = declarative_base()

# classes/tabelas do banco

class Cliente(Base):
    __tablename__ = 'clientes'
    
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String, nullable=False)
    telefone = Column("telefone", String, nullable=False, unique=True)
    endereco = Column("endereco", Text)
    
    def __init__(self, nome, telefone, endereco=None):
        self.nome = nome
        self.telefone = telefone
        self.endereco = endereco
    
    
class Pizza(Base):
    __tablename__ = 'pizzas'
    
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    sabor = Column("sabor", String, nullable=False)
    preco = Column("preco", Float, nullable=False)
    
    def __init__(self, sabor, preco):
        self.sabor = sabor
        self.preco = preco
        

class Refrigerante(Base):
    __tablename__ = 'refrigerantes'
    
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String, nullable=False)
    litro = Column("litro", Float, nullable=False)
    preco = Column("preco", Float, nullable=False)
    
    def __init__(self, nome, litro, preco):
        self.nome = nome
        self.litro = litro
        self.preco = preco
        

class Pedido(Base):
    __tablename__ = 'pedidos'
    
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    data = Column("data", Date, nullable=False)
    valor = Column("valor", Float, nullable=False)
    frete = Column("frete", Float, nullable=False)
    pagamento = Column("pagamento", String, nullable=False)
    id_cliente = Column("id_cliente", ForeignKey("clientes.id"), nullable=False)
    
    def __init__(self, data, valor, frete, pagamento, id_cliente):
        self.data = data
        self.valor = valor
        self.frete = frete
        self.pagamento = pagamento
        self.id_cliente = id_cliente


class PedidoPizza(Base):
    __tablename__ = 'pedido_pizzas'
    
    id_pedido = Column("id_pedido", ForeignKey("pedidos.id"), nullable=False)
    id_pizza = Column("id_pizza", ForeignKey("pizzas.id"), nullable=False)
    quantidade = Column("quantidade", Integer, default=1)
    
    __table_args__ = (PrimaryKeyConstraint('id_pedido', 'id_pizza'),)
    
    def __init__(self, id_pedido, id_pizza, quantidade=1):
        self.id_pedido = id_pedido
        self.id_pizza = id_pizza
        self.quantidade = quantidade
        

class PedidoRefrigerante(Base):
    __tablename__ = 'pedido_refrigerantes'
    
    id_pedido = Column("id_pedido", ForeignKey("pedidos.id"), nullable=False)
    id_refrigerante = Column("id_refrigerante", ForeignKey("refrigerantes.id"), nullable=False)
    quantidade = Column("quantidade", Integer, default=1)
    
    __table_args__ = (PrimaryKeyConstraint('id_pedido', 'id_refrigerante'),)
    
    def __init__(self, id_pedido, id_refrigerante, quantidade=1):
        self.id_pedido = id_pedido
        self.id_refrigerante = id_refrigerante
        self.quantidade = quantidade
        

class Admin(Base):
    __tablename__ = 'admins'
    
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String, nullable=False)
    email = Column("email", String, nullable=False, unique=True)
    senha = Column("senha", String, nullable=False)
    
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha
