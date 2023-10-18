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
