# Exercício 11 - Jogo da forca
# Objetivo: adivinhar uma palavra secreta.

import random

palavras = ["python", "computador", "programacao", "desenvolvimento", "teclado"]
palavra = random.choice(palavras)
letras_descobertas = []
erros = 0
max_erros = 6

print("=== Jogo da Forca ===")

while erros < max_erros:
    print("\nPalavra:", end=" ")
    for letra in palavra:
        if letra in letras_descobertas:
            print(letra, end=" ")
        else:
            print("_", end=" ")
    print()

    tentativa = input("Digite uma letra: ").lower()

    if tentativa in letras_descobertas:
        print("Você já tentou essa letra.")
        continue

    if tentativa in palavra:
        letras_descobertas.append(tentativa)
        print("Acertou!")

        if all(letra in letras_descobertas for letra in palavra):
            print("Parabéns! Você venceu!")
            break
    else:
        erros += 1
        print(f"Errado! Você tem {max_erros - erros} tentativas restantes.")
else:
    print(f"Você perdeu! A palavra era: {palavra}")
