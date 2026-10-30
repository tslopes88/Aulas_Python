# Exercício 15 - Lista de tarefas
# Objetivo: adicionar, listar e remover tarefas.

tarefas = []

while True:
    print("\n=== Lista de tarefas ===")
    print("1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Remover tarefa")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        tarefa = input("Digite a tarefa: ")
        tarefas.append(tarefa)
        print("Tarefa adicionada.")

    elif opcao == "2":
        if not tarefas:
            print("Nenhuma tarefa cadastrada.")
        else:
            for i, tarefa in enumerate(tarefas, start=1):
                print(f"{i}. {tarefa}")

    elif opcao == "3":
        if not tarefas:
            print("Nenhuma tarefa para remover.")
        else:
            posicao = int(input("Qual número da tarefa deseja remover? ")) - 1
            if 0 <= posicao < len(tarefas):
                tarefas.pop(posicao)
                print("Tarefa removida.")
            else:
                print("Posição inválida.")

    elif opcao == "4":
        print("Até logo!")
        break

    else:
        print("Opção inválida.")
