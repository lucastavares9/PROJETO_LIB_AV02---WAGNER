carrinho = []

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
        confirmacao = input("Deseja confirmar o checkout? (S/N): ")
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
