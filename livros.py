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
