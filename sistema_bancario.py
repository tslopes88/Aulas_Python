# Exercício 10 - Sistema bancário
# Objetivo: simular conta bancária com depósito, saque e saldo.

print("=== Banco do Estudante ===")

saldo = 0

while True:
    print("\n1 - Ver saldo")
    print("2 - Depositar")
    print("3 - Sacar")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        print(f"Seu saldo atual é: R$ {saldo:.2f}")

    elif opcao == "2":
        valor = float(input("Digite o valor do depósito: ").replace(",", "."))
        if valor > 0:
            saldo += valor
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("Valor inválido.")

    elif opcao == "3":
        valor = float(input("Digite o valor do saque: ").replace(",", "."))
        if valor > 0 and valor <= saldo:
            saldo -= valor
            print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("Saldo insuficiente ou valor inválido.")

    elif opcao == "4":
        print("Obrigado por usar o banco!")
        break

    else:
        print("Opção inválida.")
