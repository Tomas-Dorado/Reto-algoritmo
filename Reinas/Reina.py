

class Reina:
    def __init__(self, fila, columna):
        self.fila = fila
        self.columna = columna

    def amenaza(self, otra):
        # Verificar si esta reina amenaza a otra reina
        return (self.fila == otra.fila or
                self.columna == otra.columna or
                abs(self.fila - otra.fila) == abs(self.columna - otra.columna))
