# Exercício 9 - Controle de estoque
# Objetivo: usar listas e dicionários para gerenciar produtos.

print("=== Controle de estoque ===")

estoque = []

while True:
    print("\n1 - Adicionar produto")
    print("2 - Ver estoque")
    print("3 - Buscar produto")
    print("4 - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        produto = {}
        produto["nome"] = input("Nome do produto: ")
        produto["quantidade"] = int(input("Quantidade: "))
        produto["preco"] = float(input("Preço: ").replace(",", "."))
        estoque.append(produto)
        print("Produto adicionado.")

    elif opcao == "2":
        if not estoque:
            print("Estoque vazio.")
        else:
            for item in estoque:
                print(f"Produto: {item['nome']} | Quantidade: {item['quantidade']} | Preço: R$ {item['preco']:.2f}")

    elif opcao == "3":
        nome = input("Digite o nome do produto para buscar: ")
        encontrado = False
        for item in estoque:
            if item["nome"].lower() == nome.lower():
                print(f"Produto encontrado: {item}")
                encontrado = True
                break
        if not encontrado:
            print("Produto não encontrado.")

    elif opcao == "4":
        print("Saindo do sistema...")
        break

    else:
        print("Opção inválida.")
