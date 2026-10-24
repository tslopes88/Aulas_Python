# Exercício 4 - Conversor de temperatura
# Objetivo: converter Celsius para Fahrenheit e vice-versa.

print("=== Conversor de temperatura ===")

escala = input("Escolha a escala de entrada (C/F): ").strip().upper()
valor = float(input("Digite o valor: ").replace(",", "."))

if escala == "C":
    fahrenheit = (valor * 9 / 5) + 32
    print(f"{valor}°C = {fahrenheit:.2f}°F")
elif escala == "F":
    celsius = (valor - 32) * 5 / 9
    print(f"{valor}°F = {celsius:.2f}°C")
else:
    print("Escala inválida! Use C ou F.")
