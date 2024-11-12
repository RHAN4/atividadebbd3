import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.services.usuario_service import UsuarioService
from app.repositories.usuario_repository import UsuarioRepository
from app.config.database import Session

# MENU DE OPÇÕES
def menu():
    print("\n")
    print("\t - MENU DE OPÇÕES - ")
    print("1 - Adicionar usuário.")
    print("2 - Pesquisar um usuário.")
    print("3 - Atualizar dados de um usuário.")
    print("4 - Excluir usuário.")
    print("5 - Exibir todos os usuários cadastrados.")
    print("0 - Sair.")
    
def main():
    session = Session()
    repository = UsuarioRepository(session)
    service = UsuarioService(repository)

    # Solicitando dados para o usuário
    while True:
        menu()
        opcao = int(input("\nDigite a opção desejada: "))

        match(opcao):
            case 1:
                print("\n - Adicionar usuário -")
                nome = input("Digite o seu nome: ")
                email = input("Digite o seu email: ")
                senha = input("Digite o seu senha: ")

                service.criar_usuario(nome=nome, email=email, senha=senha)
                input("\nDigite qualquer tecla para continuar. ")
                
            case 2:
                print("\n - Pesquisa por email -")
                service.pesquisar_usuario_por_email()
                input("\nDigite qualquer tecla para continuar. ")

            case 3:
                print("\n - Atualização de dados -")
                service.atualizar_dados()
                input("\nDigite qualquer tecla para continuar. ")


            case 4:
                print("\n - Excluir usuário -")
                service.excluir_dados()
                input("Digite qualquer tecla para continuar. ")
                

            case 5:
                print("\n - Exibir todos os usuários cadastrados -")
                lista_usuarios = service.listar_todos_usuarios()
                for usuario in lista_usuarios:
                    print(f"Nome: {usuario.nome} - Email: {usuario.email} - Senha: {usuario.senha}")
                input("\nDigite qualquer tecla para continuar. ")


            case 0:
                print("Saindo...")
                break

            case _:
                print("\nDigite uma opção válida. Tente novamente.")

if __name__ == "__main__":
    os.system("cls || clear")
    main()