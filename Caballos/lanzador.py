from Caballo import CaballoAjedrez

def lanzador():
    caballo = CaballoAjedrez()
    print("Cantidad de movimientos | Posibilidades válidas")
    for movimientos in [1, 2, 32]:
        print(f"{movimientos:23} | {caballo.calcular_movimientos_totales(movimientos)}")

lanzador()