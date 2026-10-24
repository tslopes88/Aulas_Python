# Exercício 12 - Sistema de biblioteca
# Objetivo: cadastrar livros, listar e buscar por título.

biblioteca = []

while True:
    print("\n=== Biblioteca ===")
    print("1 - Cadastrar livro")
    print("2 - Listar livros")
    print("3 - Buscar livro")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        livro = {}
        livro["titulo"] = input("Título: ")
        livro["autor"] = input("Autor: ")
        livro["ano"] = int(input("Ano: "))
        biblioteca.append(livro)
        print("Livro cadastrado com sucesso!")

    elif opcao == "2":
        if not biblioteca:
            print("Nenhum livro cadastrado.")
        else:
            for livro in biblioteca:
                print(f"{livro['titulo']} - {livro['autor']} ({livro['ano']})")

    elif opcao == "3":
        busca = input("Digite o título para buscar: ").lower()
        encontrado = False
        for livro in biblioteca:
            if livro["titulo"].lower() == busca:
                print(f"Livro encontrado: {livro['titulo']} - {livro['autor']} ({livro['ano']})")
                encontrado = True
                break
        if not encontrado:
            print("Livro não encontrado.")

    elif opcao == "4":
        print("Até mais!")
        break

    else:
        print("Opção inválida.")
