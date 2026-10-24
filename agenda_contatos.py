# Exercício 8 - Agenda de contatos
# Objetivo: guardar nome, telefone e email em listas de dicionários.

print("=== Agenda de contatos ===")

agenda = []

while True:
    print("\n1 - Cadastrar contato")
    print("2 - Listar contatos")
    print("3 - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome: ")
        telefone = input("Telefone: ")
        email = input("Email: ")
        agenda.append({"nome": nome, "telefone": telefone, "email": email})
        print("Contato cadastrado com sucesso!")

    elif opcao == "2":
        if not agenda:
            print("Agenda vazia.")
        else:
            for contato in agenda:
                print(f"Nome: {contato['nome']} | Telefone: {contato['telefone']} | Email: {contato['email']}")

    elif opcao == "3":
        print("Encerrando agenda...")
        break

    else:
        print("Opção inválida.")
