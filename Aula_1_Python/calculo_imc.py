peso = float(input("Digite seu peso (kg): ").replace(",", "."))
altura = float(input("Digite sua altura (m): ").replace(",", "."))

if peso > 0 and altura > 0:
    imc = peso / (altura * altura)
    if imc < 18.5:
        print("Abaixo do peso")
    elif imc < 25:
        print("Peso normal")
    else:
        print("Acima do normal")
else:
    print("Valores inválidos!")
