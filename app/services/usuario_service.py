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

            if not nome:
                raise ValueError("Esse campo não pode estar vazio!")
            return True
            
        except TypeError as erro:
            print(f"Erro ao salvar o usuário: {erro}")
        except Exception as erro:
            print(f"Ocorreu um erro inesperado: {erro}")

    def pesquisar_usuario_por_email(self):
        try:
            # print("\n - Pesquisa por email -")
            email = input("Digite o email desejado: ")
            consulta = self.repository.pesquisar_usuario_por_email(email=email)

                # consulta = repository.session.query(Usuario).filter_by(email = email_consulta).first()
            if consulta:
                print(f"""Nome: {consulta.nome}
                      Email: {consulta.email}
                      Senha: {consulta.senha}""")
            else:
                print("Usuário não encontrado.")
            
        except TypeError as erro:
            print(f"Usuário não encontrado.")

    def atualizar_dados(self):
        try:
            # print(" - Atualização de dados - ")
            email_usuario = input("Digite o email do usuário: ")
            usuario_cadastrado = self.repository.pesquisar_usuario_por_email(email = email_usuario)

            if usuario_cadastrado:
                usuario_cadastrado.nome = input("Digite o novo nome: ")
                usuario_cadastrado.email = input("Digite o novo email: ")
                usuario_cadastrado.senha = input("Digite a nova senha: ")
                self.repository.salvar_usuario(usuario_cadastrado)
                print("Dados atualizados com sucesso.")

            else:
                print("Usuário inválido.")
        except TypeError as erro:
            print(f"Erro ao atualizar os dados: {erro}")
        except Exception as erro:
            print(f"Ocorreu um erro inesperado: {erro}")

    def excluir_dados(self):
            try:
                email = input("Digite o email do usuário: ")
                excluir_dados = self.repository.pesquisar_usuario_por_email(email)

                if excluir_dados:
                    self.repository.excluir_usuario(excluir_dados)
                    print("Usuário excluido com sucesso.")
                else:
                    print("Dados inválidos.")
                    
            except TypeError as erro:
                print(f"Erro ao excluir usuário: {erro}")
            except Exception as erro:
                print(f"Ocorreu um erro inesperado: {erro}")

    def listar_todos_usuarios(self):
        return self.repository.listar_usuarios()