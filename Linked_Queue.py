class Pila:
    def __init__(self):
        self.items = []
        self.len = 0

    def push(self, elemento):
        self.items.append(elemento)
        self.len += 1

    def pop(self):
        if self.is_empty():
            print("La pila está vacía")
            return None

        self.len -= 1
        return self.items.pop()

    def is_empty(self):
        return self.len == 0

    def __str__(self):
        return str(self.items)
