from Nodo import Nodo
from Reina import Reina




def resolver_n_reinas(n):
    soluciones = []
    pila = [Nodo([], 0)]  # Usamos una pila para realizar backtracking

    while pila:
        nodo_actual = pila.pop()
        fila_actual = nodo_actual.fila
        tablero_actual = nodo_actual.tablero

        if fila_actual == n:
            # Si hemos colocado todas las reinas, guardamos la solución
            soluciones.append(tablero_actual)
            continue

        for columna in range(n):
            nueva_reina = Reina(fila_actual, columna)
            if all(not nueva_reina.amenaza(reina) for reina in tablero_actual):
                # Si la nueva reina no es amenazada, creamos un nuevo nodo
                nuevo_tablero = tablero_actual + [nueva_reina]
                pila.append(Nodo(nuevo_tablero, fila_actual + 1))

    return soluciones


def imprimir_soluciones(n):
    soluciones = resolver_n_reinas(n)
    print(f"Para {n} reinas:")
    print(f"Total de soluciones distintas: {len(soluciones)}")
    if soluciones:
        # Convertimos una solución a un formato legible
        una_solucion = [reina.columna for reina in soluciones[0]]
        print(f"Una solución: {una_solucion}")
    else:
        print("No hay soluciones.")


if __name__ == "__main__":
    n = int(input("Ingrese el número de reinas: "))
    imprimir_soluciones(n)