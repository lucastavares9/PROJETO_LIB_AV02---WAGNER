import os
import time

def pausar():
    
    input("\nPressione Enter para continuar...")



usuario_logado = False

while True:
    print("\nBem vindo a Biblioteca Amigos TI\n\nEscolha uma das opções:\n\n======== MENU ========")

    if not usuario_logado:
        print("1- Cadastro de usuário")
        print("2- Login")

    if usuario_logado:
        print("3- Cadastrar livro")
        print("4- Listar livros cadastrados")
        print("5- Alugar livro")
        print("6- Visualizar carrinho")
        print("7- Carrinho de livros")
        print("8- Sair")

    try:
        digito = int(input("\nDigite a opção desejada: "))
    except ValueError:
        print("Por favor, digite um número válido.")
        continue

    if digito == 1:
        cadastrar_usuario(usuarios)
        time.sleep(1)
        os.system("clear")

    elif digito == 2 and not usuario_logado:
        nome_login = input("Digite seu nome para login: ")
        senha_login = input("Digite sua senha para login: ")
        usuario_logado = fazer_login(usuarios, nome_login, senha_login)
        time.sleep(1)
        os.system("clear")

    elif usuario_logado:
        if digito == 3:
            cadastro_livro(novos_livros)
            time.sleep(2)
            os.system("clear")

        elif digito == 4:
            listar_livros(novos_livros)
            time.sleep(2)
            os.system("clear")

        elif digito == 5:
            alugar_livro(novos_livros, carrinho)
            time.sleep(2)
            os.system("clear")

        elif digito == 6:
            visualizar_carrinho(carrinho)
            time.sleep(1)
            os.system("clear")

        elif digito == 7:
            carrinho_checkout(novos_livros, carrinho, usuario_logado)
            pausar()
            os.system("clear")

        elif digito == 8:
            print("Saindo do programa.")
            break

        else:
            print("Opção inválida. Tente novamente.")
    else:
        print("Acesso negado. Faça o login primeiro.")