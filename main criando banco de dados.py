from os import system
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker, declarative_base
system("cls||clear")


# Criando banco de dados.
MEU_BANCO = create_engine("sqlite:///meubanco.db")

# ORM 
# CREATE DATABASE meubanco;

# Criando conexão com banco de dados. (para haver uma comunicação)
Session = sessionmaker(bind=MEU_BANCO)
session = Session()

# Criando tabela
Base = declarative_base()

class Usuario(Base):
    __tablename__ = "usuarios"

    # Definindo campos na tabela.
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String)
    email = Column("email", String)
    senha = Column("senha", String)
    

    # Definindo atributos da classe
    def __init__(self, nome: str, email: str, senha: str):
        self.nome = nome
        self.email = email
        self.senha = senha

#  Criando tabela no banco de dados.
Base.metadata.create_all(bind=MEU_BANCO)

# Salvar no banco de dados.

print("\nSolicitando dados para o usuário")
usuario = Usuario(nome ="Marta", email="maria@gmail.com", senha = "123")
session.add(usuario)
session.commit()

usuario = Usuario(nome = "Martona", email="marta@gmail.com", senha = "456")
session.add(usuario)
session.commit()

# Listando todos os usuários do banco de dados.
print("\nExibindo todos os usuários do banco de dados.")
lista_usuarios = session.query(Usuario).all()

for usuario in lista_usuarios:
    print(f"{usuario.id} - {usuario.nome} - {usuario.senha}")

# Fechando conexão.
session.close() 