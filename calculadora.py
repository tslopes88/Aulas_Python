# Exercício 13 - Calculadora simples
# Objetivo: realizar operações básicas com menu.

print("=== Calculadora ===")

while True:
    print("\n1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Dividir")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "5":
        print("Calculadora encerrada.")
        break

    if opcao not in ["1", "2", "3", "4"]:
        print("Opção inválida.")
        continue

    n1 = float(input("Digite o primeiro número: ").replace(",", "."))
    n2 = float(input("Digite o segundo número: ").replace(",", "."))

    if opcao == "1":
        print(f"Resultado: {n1 + n2}")
    elif opcao == "2":
        print(f"Resultado: {n1 - n2}")
    elif opcao == "3":
        print(f"Resultado: {n1 * n2}")
    elif opcao == "4":
        if n2 == 0:
            print("Erro: divisão por zero.")
        else:
            print(f"Resultado: {n1 / n2}")
