import numpy as np

grid_1d = np.zeros(12)
length = len(grid_1d)
grid_1d[-3] = 1

def evolve(grid):
    new_grid = grid.copy()
    length = len(grid)
    for i in range(1, length - 1): # We start at 1 and end at length - 1 to avoid index errors.
        slice = tuple(grid[i - 1 : i + 2])
        rule_110 = {(1, 1, 1): 0, (1, 1, 0): 1, (1, 0, 1): 1, (1, 0, 0): 0,
                    (0, 1, 1): 1, (0, 1, 0): 1, (0, 0, 1): 1, (0, 0, 0): 0}
        new_grid[i] = rule_110[slice]
    return new_grid