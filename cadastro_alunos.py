# Exercício 7 - Cadastro de alunos
# Objetivo: usar dicionários para guardar dados dos alunos.

print("=== Cadastro de alunos ===")

alunos = {}

quantidade = int(input("Quantos alunos deseja cadastrar? "))

for i in range(1, quantidade + 1):
    nome = input(f"Nome do aluno {i}: ")
    nota1 = float(input("Primeira nota: ").replace(",", "."))
    nota2 = float(input("Segunda nota: ").replace(",", "."))

    media = (nota1 + nota2) / 2
    alunos[nome] = media

print("\nRelatório:")
for nome, media in alunos.items():
    print(f"{nome}: média {media:.2f}")
