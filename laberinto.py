"""
Laberinto - Un juego donde el jugador debe navegar a través de un laberinto y encontrar la salida.

Controles:
Utiliza las teclas direccionales (arriba, abajo, izquierda, derecha) para mover al jugador.

Objetivo:
Encuentra la salida del laberinto sin tocar las paredes (representadas por 'X').

"""
import pygame
import sys

pygame.init()

# Configuración de la ventana
ventana_ancho = 800
ventana_alto = 600
ventana = pygame.display.set_mode((ventana_ancho, ventana_alto))
pygame.display.set_caption("Laberinto")

# Colores
blanco = (255, 255, 255)
negro = (0, 0, 0)
rojo = (255, 0, 0)
verde = (0, 255, 0)

# Tamaño y margen del laberinto
celda_tamano = 40
celda_margen = 5

# Representación del laberinto
laberinto = [
    "XXXXXXXXXXXXXXXXXXXX",
    "X   X   X         X",
    "X X X X X X X X X X",
    "X X X X X   X X X X",
    "X X X X X X X X X X",
    "X X     X X X X X X",
    "X X X X X X X X X X",
    "X X X X   X X X X X",
    "X X X X X X X X X X",
    "X   X   X   X     X",
    "XXXXXXXXXXXXXXXXXX"
]

# Función para dibujar el laberinto


def dibujar_laberinto():
    for fila in range(len(laberinto)):
        for columna in range(len(laberinto[fila])):
            celda = laberinto[fila][columna]
            color = blanco if celda == " " else negro if celda == "X" else rojo
            pygame.draw.rect(ventana, color, [(celda_margen + celda_tamano) * columna + celda_margen,
                                              (celda_margen + celda_tamano) *
                                              fila + celda_margen,
                                              celda_tamano, celda_tamano])

# Función principal del juego


def jugar_laberinto():
    jugador_posicion = [1, 1]

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Movimiento del jugador con las teclas direccionales
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_UP] and laberinto[jugador_posicion[1] - 1][jugador_posicion[0]] == " ":
            jugador_posicion[1] -= 1
        if teclas[pygame.K_DOWN] and laberinto[jugador_posicion[1] + 1][jugador_posicion[0]] == " ":
            jugador_posicion[1] += 1
        if teclas[pygame.K_LEFT] and laberinto[jugador_posicion[1]][jugador_posicion[0] - 1] == " ":
            jugador_posicion[0] -= 1
        if teclas[pygame.K_RIGHT] and laberinto[jugador_posicion[1]][jugador_posicion[0] + 1] == " ":
            jugador_posicion[0] += 1

        ventana.fill(negro)
        dibujar_laberinto()

        # Dibujar al jugador
        jugador_rect = pygame.Rect((celda_margen + celda_tamano) * jugador_posicion[0] + celda_margen,
                                   (celda_margen + celda_tamano) *
                                   jugador_posicion[1] + celda_margen,
                                   celda_tamano, celda_tamano)
        pygame.draw.rect(ventana, verde, jugador_rect)

        pygame.display.update()


if __name__ == "__main__":
    jugar_laberinto()
