from Nodo import Nodo

class CaballoAjedrez:
    def __init__(self):
        self.nodos = {i: Nodo(i) for i in range(10)}
        self._inicializar_movimientos()

    def _inicializar_movimientos(self):
        # Definir las posibles posiciones relativas del movimiento del caballo
        movimientos_relativos = [
            (-2, -1), (-1, -2), (1, -2), (2, -1),
            (2, 1), (1, 2), (-1, 2), (-2, 1)
        ]

        # Representar el teclado como una matriz para calcular movimientos
        teclado = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
            [None, 0, None]
        ]

        # Crear un mapa de posiciones para los números
        posicion = {}
        for i, fila in enumerate(teclado):
            for j, numero in enumerate(fila):
                if numero is not None:
                    posicion[numero] = (i, j)

        # Calcular los movimientos válidos para cada número
        for numero, (x, y) in posicion.items():
            for dx, dy in movimientos_relativos:
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(teclado) and 0 <= ny < len(teclado[nx]) and teclado[nx][ny] is not None:
                    self.nodos[numero].agregar_movimiento(self.nodos[teclado[nx][ny]])

    def contar_movimientos_validos(self, nodo, movimientos_restantes, memo):
        # Caso base: si no quedan movimientos, hay una única posibilidad (quedarse en el número actual)
        if movimientos_restantes == 0:
            return 1

        # Verificar si el resultado ya está en la memoria
        if (nodo.valor, movimientos_restantes) in memo:
            return memo[(nodo.valor, movimientos_restantes)]

        # Calcular los movimientos válidos recursivamente
        total_movimientos = 0
        for siguiente in nodo.movimientos_validos:
            total_movimientos += self.contar_movimientos_validos(siguiente, movimientos_restantes - 1, memo)

        # Guardar el resultado en la memoria
        memo[(nodo.valor, movimientos_restantes)] = total_movimientos
        return total_movimientos

    def calcular_movimientos_totales(self, movimientos):
        memo = {}
        total = 0
        # Calcular los movimientos válidos desde cada número del teclado
        for nodo in self.nodos.values():
            total += self.contar_movimientos_validos(nodo, movimientos, memo)
        return total