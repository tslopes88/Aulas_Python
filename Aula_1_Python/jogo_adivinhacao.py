# Exercício 6 - Jogo da adivinhação
# Objetivo: o usuário tenta adivinhar um número escolhido aleatoriamente.

import random

print("=== Jogo da adivinhação ===")
numero_sorteado = random.randint(1, 10)

for tentativa in range(1, 4):
    palpite = int(input(f"Tentativa {tentativa}/3 - Digite um número de 1 a 10: "))

    if palpite == numero_sorteado:
        print("Parabéns! Você acertou!")
        break
    elif palpite < numero_sorteado:
        print("Tente um número maior.")
    else:
        print("Tente um número menor.")
else:
    print(f"Você perdeu! O número era {numero_sorteado}.")
