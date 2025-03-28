import random
import os
import time

def intial_grid(rows, col):
    return [[random.choice([0,1]) for _ in range(col)] for _ in range(rows)]

def display_grid(grid):
    os.system('cls' if os.name == 'nt' else 'clear')
    for row in grid:
        print(" ".join("o" if cell else "." for cell in row))

def count_live_neighbors(grid, x, y, rows, col):
    direction = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,0),(1,1),(1,-1)]
    live_neighbors = 0
    for dx, dy in direction:
        nx, ny = x+dx, y+dy
        if 0 <= nx < rows and 0 <= ny < col:
            live_neighbors += grid[nx][ny]
    return live_neighbors

def next_generation(grid, rows, col):
    new_grid = [[0 for _ in range(col)] for _ in range(rows)]
    for x in range(rows):
        for y in range(rows):
            live_neighbors = count_live_neighbors(grid, x, y, rows, col)
            if grid[x][y] == 1 and live_neighbors in [2,3]:
                new_grid[x][y] = 1
            elif grid[x][y] == 0 and live_neighbors == 3:
                new_grid[x][y] = 1
    return new_grid

def game_of_life(rows=20, col=20, generations=100):
    grid = intial_grid(rows,col)
    for _ in range(generations):
        display_grid(grid)
        grid = next_generation(grid, rows, col)
        time.sleep(1)

game_of_life()

