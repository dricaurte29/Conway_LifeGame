import pygame
import numpy as np
import pandas as pd
from utils import generacion

# Read initial matrix data from 'matriz.xlsx' file using Pandas
# The matrix should contain 0s and 1s, where 0 represents a dead cell and 1 represents a living cell
# You can either provide the initial matrix in 'matriz.xlsx' or use np.random.randint to start with a random matrix
datos = pd.read_excel('matriz.xlsx', header=None)
M = datos.values

# Time interval between generations (in milliseconds)
TIME = 100

# Dimensions of the window
WIDTH, HEIGHT = 500, 500

# Size of the pixels in the pixel art
PIXEL_SIZE = 5

# Dimensions of the matrix
MATRIX_WIDTH, MATRIX_HEIGHT = WIDTH // PIXEL_SIZE, HEIGHT // PIXEL_SIZE
SIZE = MATRIX_HEIGHT

# Uncomment the line below to start with a random matrix instead of the one from 'matriz.xlsx'
# M = np.random.randint(2, size=(SIZE, SIZE))

def draw_pixel_art(screen, matrix):
    # Draw the pixel art on the screen based on the matrix
    for y, row in enumerate(matrix):
        for x, pixel_value in enumerate(row):
            pixel_color = (214, 255, 76) if pixel_value == 1 else (0, 0, 0)
            pygame.draw.rect(screen, pixel_color, pygame.Rect(x * PIXEL_SIZE, y * PIXEL_SIZE, PIXEL_SIZE, PIXEL_SIZE))

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Conway's Game of Life")
    clock = pygame.time.Clock()

    # Generate the initial matrix using the data from 'matriz.xlsx' or the random matrix (uncommented line)
    matrix = generacion(M, SIZE)

    start_time = pygame.time.get_ticks()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        current_time = pygame.time.get_ticks()
        if current_time - start_time >= TIME:  # Change every 1000 milliseconds (1 second)
            matrix = generacion(M, SIZE)
            start_time = current_time

        screen.fill((0, 0, 0))  # Clear the screen with black color
        draw_pixel_art(screen, matrix)  # Draw the matrix on the screen
        pygame.display.flip()   # Update the screen
        clock.tick(30)          # Animation speed (frames per second)

    pygame.quit()

if __name__ == '__main__':
    main()
