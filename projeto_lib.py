import os
import time

def pausar():
    
    input("\nPressione Enter para continuar...")


def cadastrar_usuario(usuarios):
    while True:
        try:
            nome_login = input("Digite seu nome de usuario: ")

            if nome_login in usuarios:
                raise ValueError("Usuário já existe. Tente novamente.")

            if any(char.isdigit() for char in nome_login):
                raise ValueError("Nome de usuário não pode conter números. Tente novamente.")

            senha_login = input("Digite sua senha (mínimo 6 caracteres): ")

            while len(senha_login) < 6:
                raise ValueError("A senha deve ter no mínimo 6 caracteres. Tente novamente.")

            usuarios[nome_login] = senha_login
            print("Usuário cadastrado com sucesso!")
            break

        except ValueError as e:
            print(f"Erro: {e}")

def fazer_login(usuarios, nome_login, senha_login):
    try:
        if nome_login in usuarios and usuarios[nome_login] == senha_login:
            print("Login bem-sucedido!")
            return True
        else:
            print("Nome de usuário ou senha incorretos. Tente novamente.")
            return False
    except ValueError as e:
        print(f"Erro: {e}")
        return False

def cadastro_livro(novos_livros):
    while True:
        try:
            nome_livro = input("Digite nome do livro: ")

            if nome_livro in novos_livros:
                raise ValueError("Livro já cadastrado, tente novamente.")

            if not any(char.isalpha() for char in nome_livro):
                raise ValueError("Nome do livro deve conter pelo menos uma letra. Tente novamente.")

            while True:
                autor_livro = input("Informe nome do Autor: ")
                if any(char.isdigit() for char in autor_livro):
                    raise ValueError("Nome do Autor não pode conter números. Tente novamente.")
                break

            while True:
                editora_livro = input("Digite nome da Editora: ")
                if not any(char.isalpha() for char in editora_livro):
                    raise ValueError("Nome da Editora não pode conter somente números. Tente novamente.")
                break

            novos_livros[nome_livro] = {"Autor": autor_livro, "Editora": editora_livro}
            print("Livro cadastrado com sucesso!")
            break

        except ValueError as e:
            print(f"Erro: {e}")

def listar_livros(novos_livros):
    print("\n======== Lista de Livros Cadastrados ========")
    for livro, detalhes in novos_livros.items():
        print(f"Nome: {livro}, Autor: {detalhes['Autor']}, Editora: {detalhes['Editora']}")
    print("==============================================")

def alugar_livro(novos_livros, carrinho):
    nome_livro = input("Digite o nome do livro que deseja alugar: ")
    if nome_livro in novos_livros:
        carrinho.append(nome_livro)
        print(f"Livro '{nome_livro}' adicionado ao carrinho.")
    else:
        print("Livro não encontrado. Verifique o nome e tente novamente.")

def carrinho_checkout(novos_livros, carrinho, sistema_liberado):
    if not sistema_liberado:
        print("Sistema não liberado. Faça o login primeiro.")
        return

    if not carrinho:
        print("Seu carrinho está vazio.")
    else:
        print("\n======= Carrinho de Livros =======")
        for livro in carrinho:
            print(f"- {livro}")
        print("=================================")
        total = calcular_total(novos_livros, carrinho)
        print(f"Total a pagar: R$ {total}")
        confirmacao = input("\nDeseja confirmar o checkout? (S/N): ")
        if confirmacao.upper() == "S":
            processar_checkout(novos_livros, carrinho)
            print("\nCheckout concluído com sucesso!")
            carrinho.clear()
        else:
            print("Checkout cancelado.")

def visualizar_carrinho(carrinho):
    print("\n======= Carrinho de Livros =======")
    for livro in carrinho:
        print(f"- {livro}")
    print("=================================")

def calcular_total(novos_livros, carrinho):
    total = 0
    for livro in carrinho:
        if livro in novos_livros:
            total += 10  
    return total

def processar_checkout(novos_livros, carrinho):
    for livro in carrinho:
          if livro in novos_livros:
            print(f"Livro '{livro}' processado no checkout.")
            
usuarios = {}
novos_livros = {}
carrinho = []
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
            time.sleep(2)
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