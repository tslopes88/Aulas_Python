import random

print("=== LOTERIA ===")
print("Digite 6 números de 1 a 60")

aposta = []

for i in range(6):
    while True:
        try:
            numero = int(input(f"Número {i + 1}: "))
            if 1 <= numero <= 60 and numero not in aposta:
                aposta.append(numero)
                break
            print("Número inválido. Escolha outro entre 1 e 60 e não repita.")
        except ValueError:
            print("Digite apenas números inteiros.")

aposta = sorted(aposta)
print(f"Sua aposta: {aposta}")

sorteio = sorted(random.sample(range(1, 61), 6))
print(f"Números sorteados: {sorteio}")

acertos = len(set(aposta) & set(sorteio))
print(f"Você acertou {acertos} número(s).")

if acertos == 6:
    print("Parabéns! Você ganhou a Mega-Sena!")
elif acertos >= 3:
    print("Você ganhou um prêmio menor!")
else:
    print("Tente novamente na próxima sorte!")
