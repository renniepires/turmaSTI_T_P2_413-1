import numpy as np

class fila:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.inicio = 0
        self.final = -1
        self.numero_elementos = 0
        self.valores = np.empty(self.capacidade, dtype=int)

    def fila_vazia(self):
        return self.numero_elementos == 0

    def fila_cheia(self):
        return self.numero_elementos == self.capacidade
    
    def enfileirar(self, valor):
        if self.fila_cheia():
            print('A fila está cheia')
            return
        if self.final == self.capacidade - 1:
            self.final = -1
        self.final += 1
        self.valores[self.final] = valor
        self.numero_elementos += 1

    def desenfileirar(self):
        if self.fila_vazia():
            print('A fila jĂĄ estĂĄ vazia')
            return
        temp = self.valores[self.inicio]
        self.inicio += 1
        if self.inicio == self.capacidade - 1:
            self.inicio = 0
        else:
            self.numero_elementos -= 1
            return temp

    def primeiro(self):
        if self.fila_vazia():
            return -1
        else:
            return self.valores[self.inicio]

    def visualizar(self):
            if not self.fila_vazia():
                print("Itens da Fila:")
                for i in range(self.numero_elementos):
                  print(self.valores[i])
            else:
                print("A pilha estĂĄ vazia. NĂŁo hĂĄ itens para visualizar.")


fila1 = fila(6)
fila1.enfileirar(9)
fila1.enfileirar(8)
fila1.enfileirar(2)
fila1.enfileirar(1)

print('O primeiro da fila..: ',fila1.primeiro())
print('================')
fila1.visualizar()
fila1.desenfileirar()
print('================')
print('O primeiro da fila..: ',fila1.primeiro())