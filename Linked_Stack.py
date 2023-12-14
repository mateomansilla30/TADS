class Nodo:
    def __init__(self, dato, proximo=None):
        self.dato = dato
        self.prox = proximo

class PilaEnlazada:
    def __init__(self):
        self.cima = None
        self.len = 0

    def push(self, elemento):
        nuevo_nodo = Nodo(elemento)
        nuevo_nodo.prox = self.cima
        self.cima = nuevo_nodo
        self.len += 1

    def pop(self):
        if self.len == 0:
            print("La pila no contiene elementos")
            return None

        elemento_eliminado = self.cima.dato
        self.cima = self.cima.prox
        self.len -= 1

        return elemento_eliminado

    def is_empty(self):
        return self.len == 0

    def imprimir(self):
        actual = self.cima
        while actual is not None:
            print(actual.dato)
            actual = actual.prox
