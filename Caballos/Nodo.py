class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.movimientos_validos = []

    def agregar_movimiento(self, nodo):
        self.movimientos_validos.append(nodo)