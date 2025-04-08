from Caballo import CaballoAjedrez
import pygame
import sys

def lanzador():
    caballo = CaballoAjedrez()
    print("Cantidad de movimientos | Posibilidades válidas")
    for movimientos in [1, 2,3,5,8,10,15,18,21,23, 32]:
        print(f"{movimientos:23} | {caballo.calcular_movimientos_totales(movimientos)}")

lanzador()
