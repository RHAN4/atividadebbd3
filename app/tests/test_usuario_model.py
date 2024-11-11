import pytest
from app.models.usuario_model import Usuario

# @pytest.fixture
# def usuario_valido():
#     usuario = Usuario("José", "jose@gmail.com", "1234")
#     return usuario

# def test_validar_nome(usuario_valido):
#     assert usuario_valido.nome == "José"

# def test_validar_email(usuario_valido):
#     assert usuario_valido.email == "jose@gmail.com"

# def test_validar_senha(usuario_valido):
#     assert usuario_valido.senha == "1234"

def test_nome_invalido():
    with pytest.raises(TypeError, match="O nome deve ser um texto."):
        Usuario(2, "jose@gmail.com", "1234")

def test_email_invalido():
    with pytest.raises(TypeError, match="Email deve ser um texto."):
        Usuario("José", 20, "1234")

def test_senha_invalida():
    with pytest.raises(TypeError, match="Senha deve ser um texto."):
        Usuario("José", "jose@gmail.com", 1234)