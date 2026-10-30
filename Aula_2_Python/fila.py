from collections import deque

fila = deque()

fila.append("Ana")
fila.append("Bruno")
fila.append("Carla")

print(fila.popleft())
print(fila)


class Fila:
    def __init__(self):
        self._itens = deque()

    @property
    def itens(self):
        return self._itens

    def enfileirar(self, item):
        self._itens.append(item)

    def esta_vazia(self):
        return len(self._itens) == 0

    def tamanho(self):
        return len(self._itens)

    def desenfileirar(self):
        if self.esta_vazia():
            raise IndexError("Não é possível desenfileirar, a fila está vazia")
        return self._itens.popleft()

    def frente(self):
        if self.esta_vazia():
            raise IndexError("A fila está vazia")
        return self._itens[0]

    def esvaziar(self):
        self._itens.clear()

    def __str__(self):
        return f"Frente -> {list(self._itens)} <- Fim"

f = Fila()

print(f.esta_vazia())

f.enfileirar("A")
f.enfileirar("B")
f.enfileirar("C")

print(f)

print(f.tamanho())
print(f.frente())

print(f.desenfileirar())
print(f)
