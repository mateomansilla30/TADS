class Nodo:
    def __init__(self, cargo, prox=None):
        self.cargo = cargo
        self.prox = prox

class ListaEnlazada:
    def __init__(self):
        self.primero = None
        self.len = 0

    def insert(self, i, dato):
        if i < 0 or i > self.len:
            print("Índice fuera de rango")
            return

        nuevo_nodo = Nodo(dato)

        if i == 0:
            nuevo_nodo.prox = self.primero
            self.primero = nuevo_nodo
        else:
            nodo_anterior = self.primero
            for _ in range(1, i):
                nodo_anterior = nodo_anterior.prox

            nuevo_nodo.prox = nodo_anterior.prox
            nodo_anterior.prox = nuevo_nodo

        self.len += 1

    def pop_i(self, i: int | None = None):
        if i is None:
            i = self.len - 1

        if i < 0 or i >= self.len:
            print("Índice fuera de rango")
            return None

        if i == 0:
            dato_eliminado = self.primero
            self.primero = self.primero.prox
        else:
            n_ant = self.primero
            for pos in range(1, i):
                n_ant = n_ant.prox

            dato_eliminado = n_ant.prox
            n_ant.prox = dato_eliminado.prox

        self.len -= 1
        return dato_eliminado.cargo if dato_eliminado else None

    def imprimir(self):
        actual = self.primero
        while actual is not None:
            print(actual.cargo)
            actual = actual.prox

    def __len__(self):
        return self.len
