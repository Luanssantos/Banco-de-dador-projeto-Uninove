from sqlalchemy import create_engine
from models import Base

engine = create_engine('sqlite:///loja.db')

Base.metadata.create_all(engine)

print("Banco de dados e tabelas criados com sucesso!")
