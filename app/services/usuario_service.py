from models.usuario_model import Usuario
from repositories.usuario_repository import UsuarioRepository

class UsuarioService:
    def __init__(self, repository: UsuarioRepository):
        self.repository = repository

    def criar_usuario(self, nome: str, email: str, senha: str):
        try:
            usuario = Usuario(nome=nome, email=email, senha=senha)

            novo_usuario = self.repository.pesquisar_usuario_por_email(usuario.email)

            if novo_usuario:
                print("Usuário já cadastrado!")
                return
            
            self.repository.salvar_usuario(usuario)
            print("\nUsuário cadastrado.")

        except TypeError as erro:
            print(f"Erro ao salvar o usuário: {erro}")
        except Exception as erro:
            print(f"Ocorreu um erro inesperado: {erro}")

    def pesquisar_usuario_por_email(self, email: str):
        try:
            print("\n - Pesquisa por email -")
            email = input("Digite o email desejado: ")
            consulta = self.repository.pesquisar_usuario_por_email(email=email)

                # consulta = repository.session.query(Usuario).filter_by(email = email_consulta).first()
            if consulta:
                print(f"Nome: {usuario.nome} - Email: {usuario.email} - Senha: {usuario.senha}")
            else:
                print("Usuário não encontrado.")
            
            input("Precione qualquer tecla para continuar.")
        except TypeError as erro:
            print(f"Usuário não encontrado.")


    def listar_todos_usuarios(self):
        return self.repository.listar_usuarios()