from sqlalchemy import create_engine
from models import Base

# Cria o banco de dados SQLite chamado loja.db
engine = create_engine('sqlite:///loja.db')

# Cria as tabelas definidas em models.py
Base.metadata.create_all(engine)

print("Banco de dados e tabelas criados com sucesso!")
