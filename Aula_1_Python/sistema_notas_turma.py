import os


def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")


def ler_numero(mensagem):
    while True:
        try:
            return float(input(mensagem).replace(",", "."))
        except ValueError:
            print("Valor inválido! Digite um número.")


def let_nota(numero_do_aluno):
    while True:
        nota = ler_numero(f"Nota do aluno {numero_do_aluno}: ")
        if 0 <= nota <= 10:
            return nota
        print("Nota inválida! Digite um valor entre 0 e 10.")


def sistema_diario():
    quantidade = int(input("Quantos alunos? "))

    total = 0
    maior = 0
    menor = 10
    aprovados = 0
    reprovados = 0

    for aluno in range(1, quantidade + 1):
        nota = let_nota(aluno)
        total += nota

        if nota > maior:
            maior = nota
        if nota < menor:
            menor = nota

        if nota >= 6:
            aprovados += 1
        else:
            reprovados += 1

    media = total / quantidade if quantidade > 0 else 0

    print("\n=== Resultado da turma ===")
    print(f"Média: {media:.2f}")
    print(f"Maior nota: {maior:.1f}")
    print(f"Menor nota: {menor:.1f}")
    print(f"Aprovados: {aprovados}")
    print(f"Reprovados: {reprovados}")


if __name__ == "__main__":
    limpar_tela()
    sistema_diario()
