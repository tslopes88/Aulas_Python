# Exercício 5 - Média de notas
# Objetivo: ler várias notas e mostrar a média e situação.

print("=== Média de notas ===")

quantidade = int(input("Quantas notas você vai informar? "))
notas = []

for i in range(1, quantidade + 1):
    nota = float(input(f"Nota {i}: ").replace(",", "."))
    notas.append(nota)

media = sum(notas) / quantidade
print(f"Média: {media:.2f}")

if media >= 7:
    print("Situação: Aprovado")
elif media >= 5:
    print("Situação: Recuperação")
else:
    print("Situação: Reprovado")
