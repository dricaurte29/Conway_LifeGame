# Conway's Game of Life



Conway's Game of Life is a cellular automaton devised by mathematician John Horton Conway in 1970. It is a zero-player game, meaning that its evolution is determined by its initial state, requiring no further input. The game follows simple rules but can exhibit complex and fascinating patterns.

## Rules of the Game

- The game takes place on an infinite two-dimensional grid of cells.
- Each cell can be in one of two states: alive (1) or dead (0).
- The state of each cell evolves based on its current state and the state of its eight neighbors (horizontal, vertical, and diagonal).
- If a living cell has fewer than two living neighbors, it dies due to underpopulation.
- If a living cell has more than three living neighbors, it dies due to overpopulation.
- If a dead cell has exactly three living neighbors, it becomes alive due to reproduction.
- All changes to the cells' states happen simultaneously, which creates generations of cell configurations.

## How to Use

1. Ensure you have the required libraries installed. The project uses the following libraries:
   - Python's NumPy for array operations
   - Python's Pandas for reading the initial matrix from the 'matriz.xlsx' file
   - Python's Pygame for visualization

2. If you want to start the game with a specific initial matrix, you can provide it in the 'matriz.xlsx' file. The matrix should contain 0s and 1s, where 0 represents a dead cell and 1 represents a living cell. If you prefer to start with a random initial configuration, you can uncomment the line in 'game.py' that generates a random matrix.

3. Run 'game.py' to start the simulation. The game will visualize the evolution of the cells in a Pygame window. The simulation will automatically update every 1 second (adjustable using the `TIME` variable).

4. Close the Pygame window to stop the simulation.

## Requirements

To run this project, you need the following libraries:

- NumPy
- Pandas
- Pygame

You can install them using pip:

