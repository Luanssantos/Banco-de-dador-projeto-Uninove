from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Cadastro

engine = create_engine('sqlite:///loja.db')
Session = sessionmaker(bind=engine)
session = Session()


novo_usuario = Cadastro(nome="Maria", email="maria@email.com", senha="123456")
session.add(novo_usuario)
session.commit()

print("Usuário cadastrado com sucesso!")