from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime

Base = declarative_base()

class Produto(Base):
    __tablename__ = 'produtos'
    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    preco = Column(Float, nullable=False)
    estoque = Column(Integer, nullable=False)

    vendas = relationship("Venda", back_populates="produto")


class Cadastro(Base):
    __tablename__ = 'cadastro'
    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    senha = Column(String, nullable=False)

    vendas = relationship("Venda", back_populates="cliente")


class Venda(Base):
    __tablename__ = 'vendas'
    id = Column(Integer, primary_key=True)
    produto_id = Column(Integer, ForeignKey('produtos.id'), nullable=False)
    cliente_id = Column(Integer, ForeignKey('cadastro.id'), nullable=True)
    quantidade = Column(Integer, nullable=False)
    valor_total = Column(Float, nullable=False)
    data_venda = Column(DateTime, default=datetime.utcnow, nullable=False)
    status = Column(String, default="concluída", nullable=False)

    produto = relationship("Produto", back_populates="vendas")
    cliente = relationship("Cadastro", back_populates="vendas")