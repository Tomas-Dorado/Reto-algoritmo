from Caballo import CaballoAjedrez
import pygame
import sys

def lanzador():
    caballo = CaballoAjedrez()
    print("Cantidad de movimientos | Posibilidades válidas")
    for movimientos in [1, 2, 32]:
        print(f"{movimientos:23} | {caballo.calcular_movimientos_totales(movimientos)}")

lanzador()

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((600, 600))
    pygame.display.set_caption("Movimientos del Caballo")
    clock = pygame.time.Clock()

    movimientos = int(input("Ingrese la cantidad de movimientos: "))
    caballo = CaballoAjedrez()
    posiciones = caballo.calcular_movimientos_posibles(movimientos)

    # Dibujar el tablero
    def dibujar_tablero():
        colores = [(255, 255, 255), (0, 0, 0)]
        for fila in range(8):
            for columna in range(8):
                color = colores[(fila + columna) % 2]
                pygame.draw.rect(screen, color, pygame.Rect(columna * 75, fila * 75, 75, 75))

    # Dibujar los movimientos del caballo
    def dibujar_movimientos(posiciones):
        for pos in posiciones:
            x, y = pos
            pygame.draw.circle(screen, (0, 255, 0), (y * 75 + 37, x * 75 + 37), 10)

    # Dibujar la posición inicial del caballo
    def dibujar_caballo(pos):
        x, y = pos
        pygame.draw.circle(screen, (255, 0, 0), (y * 75 + 37, x * 75 + 37), 15)

    # Suponiendo que el caballo comienza en (0, 0)
    posicion_inicial = (0, 0)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))
        dibujar_tablero()
        dibujar_movimientos(posiciones)
        dibujar_caballo(posicion_inicial)
        pygame.display.flip()
        clock.tick(30)

    pygame.quit()