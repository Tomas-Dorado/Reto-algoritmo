import pygame

def simulador_caballo():
    pygame.init()
    ancho, alto = 3, 4
    tam_celda = 100
    pantalla = pygame.display.set_mode((ancho * tam_celda, alto * tam_celda))
    pygame.display.set_caption("Simulación del Caballo")
    reloj = pygame.time.Clock()

    tablero = [[0 for _ in range(ancho)] for _ in range(alto)]
    movimientos_caballo = [
        (2, 1), (1, 2), (-1, 2), (-2, 1),
        (-2, -1), (-1, -2), (1, -2), (2, -1)
    ]
    x, y = 0, 0  # Posición inicial del caballo
    tablero[y][x] = 1

    print("Simulación del movimiento del caballo en un tablero 3x4:")
    corriendo = True
    while corriendo:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                corriendo = False

        pantalla.fill((255, 255, 255))  # Fondo blanco

        # Dibujar el tablero
        for fila in range(alto):
            for columna in range(ancho):
                color = (200, 200, 200) if (fila + columna) % 2 == 0 else (100, 100, 100)
                pygame.draw.rect(pantalla, color, (columna * tam_celda, fila * tam_celda, tam_celda, tam_celda))

        # Dibujar el caballo
        pygame.draw.circle(pantalla, (0, 0, 255), (x * tam_celda + tam_celda // 2, y * tam_celda + tam_celda // 2), tam_celda // 3)

        # Calcular movimientos válidos
        posibles_movimientos = []
        for dx, dy in movimientos_caballo:
            nx, ny = x + dx, y + dy
            if 0 <= nx < ancho and 0 <= ny < alto and tablero[ny][nx] == 0:
                # Evitar las esquinas inferiores
                if not ((nx == 0 and ny == alto - 1) or (nx == ancho - 1 and ny == alto - 1)):
                    posibles_movimientos.append((nx, ny))

        # Actualizar posición del caballo
        if posibles_movimientos:
            x, y = posibles_movimientos[0]  # Selecciona el primer movimiento válido
            tablero[y][x] += 1
        else:
            print("No hay más movimientos posibles.")
            corriendo = False

        pygame.display.flip()
        reloj.tick(1)  # Un movimiento por segundo

    print("Tablero final:")
    for fila in tablero:
        print(fila)

    pygame.quit()

simulador_caballo()
