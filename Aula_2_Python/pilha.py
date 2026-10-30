pilha = []
pilha.append("A")
pilha.append("B")
pilha.append("C")

print(pilha.pop())

print(pilha)


class Pilha:
    def __init__(self):
        self.itens = []

    @property
    def _itens(self):
        return self.itens

    def empilhar(self, item):
        self.itens.append(item)

    def esta_vazia(self):
        return len(self.itens) == 0

    def tamanho(self):
        return len(self.itens)

    def desempilhar(self):
        if self.esta_vazia():
            raise IndexError("Desempilhar de uma pilha vazia")
        return self.itens.pop()

    def topo(self):
        if self.esta_vazia():
            raise IndexError("Topo de uma pilha vazia")
        return self.itens[-1]

    def esvaziar(self):
        self.itens = []

    def __str__(self):
        return f"Pilha({self.itens}) <- topo"


p = Pilha()

print(p.esta_vazia())

p.empilhar("A")
p.empilhar("B")
p.empilhar("C")
print(p)

p.desempilhar()

print(p.topo())
print(p.tamanho())


def inverter(texto):
    x = Pilha()
    for letra in texto:
        x.empilhar(letra)
    resultado = ""
    while not x.esta_vazia():
        resultado += x.desempilhar()
    return resultado


print(inverter("Thiago"))
