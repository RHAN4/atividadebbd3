from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import declarative_base
from app.config.database import db

Base = declarative_base()

class Usuario(Base):
    # Definindo caracteristicas da tabela:
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(150))
    email = Column(String(150), unique=True)
    senha = Column(String(150))

    # Definindo caracteristicas da classe:
    def __init__(self, nome: str, email: str, senha: str) -> None:
        self.nome = self._verificar_nome(nome)
        self.email = email
        self.senha = senha

    def _verificar_nome(self, nome):
        if not isinstance(nome, str) or not nome.strip():
            raise TypeError("O nome deve ser um texto")

# Criando tabela no banco de dados:
Base.metadata.create_all(bind=db)