import pygame
import numpy as np
import random

class Grid():
    # Initializer
    def __init__(self, width, height, scale, offset):
        self.scale = scale
        self.columns = int(height / 2)
        self.rows = int(width / 2)
        self.size(self.rows, self.columns)
        self.grid_array = np.ndarray(shape=(self.size))
        self.offest = offset

    # Initialize random 2D array
    def random2d_array(self):
        for x in range(self.rows):
            for y in range(self.columns):
                self.grid_array[x][y] = random.randint(0,1)

    # The game
    def conway(self, off_color, on_color, surface):
        # Draw the board
        for x in range(self.rows):
            for y in range(self.columns):
                y_pos = y * self.scale
                x_pos = x * self.scale

                if (self.grid_array[x][y] == 1):
                    pygame.draw.rect(surface, on_color, [x_pos, y_pos, self.scale - self.offest, self.scale - self.offest])
                else:
                    pygame.draw.rect(surface, off_color, [x_pos, y_pos, self.scale - self.offest, self.scale - self.offest])

        # Update the cells
        next = np.ndarray(shape=(self.size))
        for x in range(self.rows):
            for y in range(self.columns):
                state = self.grid_array[x][y]
                neighbours = self.get_neighbours(x, y)
                if (state == 0 and neighbours == 3):
                    next[x][y] = 1
                elif (state == 1 and (neighbours < 2 or neighbours > 3)):
                    next[x][y] = 0
                else:
                    next[x][y] = state

        self.grid_array = next