import pygame
import numpy as np
import pandas as pd
from utils import generacion


datos = pd.read_excel('matriz.xlsx', header=None)

M = datos.values

TIME = 100

# Dimensiones de la ventana
WIDTH, HEIGHT = 500, 500

# Tamaño de los píxeles en el pixel art
PIXEL_SIZE = 5

# Dimensiones de la matriz
MATRIX_WIDTH, MATRIX_HEIGHT = WIDTH // PIXEL_SIZE, HEIGHT // PIXEL_SIZE
SIZE = MATRIX_HEIGHT

#M = np.random.randint(2, size=(SIZE, SIZE))

def draw_pixel_art(screen, matrix):
    for y, row in enumerate(matrix):
        for x, pixel_value in enumerate(row):
            pixel_color = (214, 255, 76) if pixel_value == 1 else (0, 0, 0)
            pygame.draw.rect(screen, pixel_color, pygame.Rect(x * PIXEL_SIZE, y * PIXEL_SIZE, PIXEL_SIZE, PIXEL_SIZE))

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Conway's Game of Life")
    clock = pygame.time.Clock()

    matrix = generacion(M,SIZE)
    start_time = pygame.time.get_ticks()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        current_time = pygame.time.get_ticks()
        if current_time - start_time >= TIME:  # Cambiar cada 1000 milisegundos (1 segundo)
            matrix = generacion(M,SIZE)
            start_time = current_time

        screen.fill((0, 0, 0))  # Limpia la pantalla con color negro
        draw_pixel_art(screen, matrix)  # Dibuja la matriz en la pantalla
        pygame.display.flip()   # Actualiza la pantalla
        clock.tick(30)          # Velocidad de la animación (cuadros por segundo)

    pygame.quit()

if __name__ == '__main__':
    main()
