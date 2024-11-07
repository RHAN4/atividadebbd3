from models.usuario_model import Usuario
from services.usuario_service import UsuarioService
from repositories.usuario_repository import UsuarioRepository
from config.database import Session
import os

# MENU DE OPÇÕES
def menu():
    print("\n")
    print("\t - MENU DE OPÇÕES - ")
    print("""  \t1 - Adicionar usuário. 
        2 - Pesquisar um usuário. 
        3 - Atualizar dados de um usuário.
        4 - Excluir usuário.
        5 - Exibir todos os usuários cadastrados
        0 - Sair.""")
    
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
                print("\n - Adicionando usuário -")
                nome = input("Digite o seu nome: ")
                email = input("Digite o seu email: ")
                senha = input("Digite o seu senha: ")

                service.criar_usuario(nome=nome, email=email, senha=senha)
                
            case 2:
                print("\n - Pesquisa por email -")
                # email = input("Digite o email desejado: ")
                service.pesquisar_usuario_por_email()
                # service.session.query(Usuario).filter_by(email = email).first()
                # print("\n - Pesquisa por email -")
                # # consulta = repository.pesquisar_usuario_por_email(email=email_consulta)

                # consulta = repository.session.query(Usuario).filter_by(email = email_consulta).first()
                # if consulta:
                #     print(f"Nome: {usuario.nome} - Email: {usuario.email} - Senha: {usuario.senha}")
                # else:
                #     print("Usuário não encontrado.")
                
                # input("Presse qualquer tecla!")

            case 3:
                print("\n - Atualização de dados -")
                # email = input("Digite o email do usuário: ")
                service.atualizar_dados()


            case 4:
                print("\n - Excluir usuário -")
                service.excluir_dados()
                

            case 5:
                print("\n - Exibir todos os usuários cadastrados -")
                lista_usuarios = service.listar_todos_usuarios()
                for usuario in lista_usuarios:
                    print(f"Nome: {usuario.nome} - Email: {usuario.email} - Senha: {usuario.senha}")


            case 0:
                print("Saindo...")
                break

            case _:
                print("Digite uma opção válida.")

if __name__ == "__main__":
    os.system("cls || clear")
    main()