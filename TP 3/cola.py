class _Nodo:
    def __init__(self, dato, prox=None):
        self.dato = dato
        self.prox = prox

class Cola:
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def encolar(self, dato):
        """
        Encola el elemento al final
        Pre: la cola NO está vacía.
        Pos: se encola el elemento
        """
        nodo = _Nodo(dato)
        if self.esta_vacia():
            self.primero = nodo
        else:
            self.ultimo.prox = nodo
        self.ultimo = nodo

    def desencolar(self):
        """
        Desencola el elemento que está en el primero de la cola
        y lo devuelve.
        Pre: la cola NO está vacía.
        Pos: el nuevo primero es el que estaba siguiente al primero anterior
        """
        if self.esta_vacia():
            raise ValueError("cola vacía")
        dato = self.primero.dato
        self.primero = self.primero.prox
        if self.primero is None:
            self.ultimo = None
        return dato

    def ver_primero(self):
        """
        Devuelve el elemento que está en el primero de la cola.
        Pre: la cola NO está vacía.
        """
        if self.esta_vacia():
            raise ValueError("cola vacía")
        return self.primero.dato

    def esta_vacia(self):
        return self.primero is None