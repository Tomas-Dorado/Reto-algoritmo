import pygame

def visualizar(n, soluciones):
    if not soluciones:
        print("No hay soluciones para visualizar.")
        return

    # Inicializamos pygame
    pygame.init()
    ancho_celda = 60
    alto_celda = 60
    ancho_tablero = n * ancho_celda
    alto_tablero = n * alto_celda
    pantalla = pygame.display.set_mode((ancho_tablero, alto_tablero))
    pygame.display.set_caption("Visualización de las Reinas")

    # Colores
    color_blanco = (255, 255, 255)
    color_negro = (0, 0, 0)
    color_reina = (255, 0, 0)

    # Seleccionamos la primera solución para visualizar
    solucion = soluciones[0]

    # Bucle principal de pygame
    corriendo = True
    while corriendo:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                corriendo = False

        # Dibujamos el tablero
        for fila in range(n):
            for columna in range(n):
                color = color_blanco if (fila + columna) % 2 == 0 else color_negro
                pygame.draw.rect(pantalla, color, (columna * ancho_celda, fila * alto_celda, ancho_celda, alto_celda))

        # Dibujamos las reinas
        for reina in solucion:
            x = reina.columna * ancho_celda + ancho_celda // 2
            y = reina.fila * alto_celda + alto_celda // 2
            pygame.draw.circle(pantalla, color_reina, (x, y), ancho_celda // 3)

        pygame.display.flip()

    pygame.quit()

# Llamamos a la función de visualización
soluciones = resolver_n_reinas(n)
visualizar_reinas(n, soluciones)