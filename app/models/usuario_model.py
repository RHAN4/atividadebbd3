from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import declarative_base
from app.config.database import db

Base = declarative_base()

class Usuario(Base):
    # Definindo caracteristicas da tabela:
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(150))
    email = Column(String(150), unique=False)
    senha = Column(String(150))

    # Definindo caracteristicas da classe:
    def __init__(self, nome: str, email: str, senha: str) -> None:
        self.nome = self._verificar_nome(nome)
        self.email = self._verificar_email(email)
        self.senha = self._verificar_senha(senha)

    def _verificar_nome(self, nome):
        if not isinstance(nome, str) or not nome.strip():
            raise TypeError("O nome deve ser um texto.")
        return nome
        
    def _verificar_email(self, email):
        if not isinstance(email, str) or not email.strip():
            raise TypeError("Email deve ser um texto.")
        return email

    def _verificar_senha(self, senha):
        if not isinstance(senha, str) or not senha.strip():
            raise TypeError("Senha deve ser um texto.")
        return senha


# Criando tabela no banco de dados:
Base.metadata.create_all(bind=db)