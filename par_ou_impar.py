# Exercício 14 - Jogo de par ou ímpar
# Objetivo: o usuário joga contra o computador.

import random

print("=== Par ou Ímpar ===")

while True:
    escolha = input("Escolha 'P' para par ou 'I' para ímpar: ").upper()
    numero = int(input("Digite um número de 0 a 10: "))
    pc = random.randint(0, 10)

    total = numero + pc
    resultado = "PAR" if total % 2 == 0 else "ÍMPAR"

    print(f"Você escolheu {escolha} e o computador escolheu {pc}.")
    print(f"Total: {total} ({resultado})")

    if escolha == resultado[:1]:
        print("Você venceu!")
    else:
        print("Você perdeu!")

    continuar = input("Quer jogar de novo? (s/n): ").lower()
    if continuar != "s":
        break
