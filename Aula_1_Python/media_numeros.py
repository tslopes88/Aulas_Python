quantidade = int(input("Quantos números? "))
soma = 0

for i in range(quantidade):
    numero = float(input(f"Número {i + 1}: ").replace(",", "."))
    soma += numero

print(f"Média: {soma / quantidade}")
