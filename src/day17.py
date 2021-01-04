import itertools
from copy import deepcopy

def make_grid(lines):
    grid = {}
    for y,line in enumerate(lines):
        cube = {(x,y,0,0):(1 if c == '#' else 0) for x,c in enumerate(line)}
        grid.update(cube)
    return grid

def grow(grid):
    grid_copy = deepcopy(grid)
    for x,y,z,w in grid_copy:
        for xo,yo,zo,wo in itertools.product([0,1,-1], repeat=4):
            neighbor = (x+xo,y+yo,z+zo,w+wo)
            if neighbor not in grid:
                grid[neighbor] = 0

def change(grid):
    grid_copy = deepcopy(grid)
    for (x,y,z,w), value in grid_copy.items():
        active_neighbors = 0
        for xo,yo,zo,wo in itertools.product([0,1,-1], repeat=4):
            if (xo,yo,zo,wo) == (0,0,0,0):
                continue
            neighbor = (x+xo,y+yo,z+zo,w+wo)
            if neighbor in grid_copy and grid_copy[neighbor] == 1:
                active_neighbors += 1
        if value == 1 and active_neighbors not in (2,3):
            grid[(x,y,z,w)] = 0
        if value == 0 and active_neighbors == 3:
            grid[(x,y,z,w)] = 1

def run(grid):
    for i in range(6):
        grow(grid)
        change(grid)
    return list(grid.values()).count(1)

def main(inp):
    with open(inp) as f:
        lines = f.read().splitlines()
    grid = make_grid(lines)
    res2 = run(grid)
    return None, res2

if __name__ == '__main__':
    res1, res2 = main('../input/input17.txt')
    print('day17.1:', res1)
    print('day17.2:', res2)
