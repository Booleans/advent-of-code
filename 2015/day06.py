import numpy as np
import re

with open('inputs/day06.txt') as f:
    instructions = tuple(line.strip() for line in f)

grid = np.zeros(shape=(1000, 1000))

for instruction in instructions:
    command = re.search(r'toggle|on|off', instruction).group()
    matches = [int(match) for match in re.findall(r'(\d{1,3})', instruction)]
    x_start, y_start, x_end, y_end = matches

    x_range = range(x_start, x_end+1)
    y_range = range(y_start, y_end+1)

    if command == 'toggle':
        grid[x_start:x_end+1, y_start:y_end+1] = np.logical_not(grid[x_start:x_end+1, y_start:y_end+1])
    elif command == 'on':
        grid[x_start:x_end+1, y_start:y_end+1] = 1
    elif command == 'off':
        grid[x_start:x_end+1, y_start:y_end+1] = 0
    
print(f'After following the instructions {np.sum(grid):.0f} lights are lit.')

grid = np.zeros(shape=(1000, 1000))

for instruction in instructions:
    command = re.search(r'toggle|on|off', instruction).group()
    matches = [int(match) for match in re.findall(r'(\d{1,3})', instruction)]
    x_start, y_start, x_end, y_end = matches

    if command == 'toggle':
        grid[x_start:x_end+1, y_start:y_end+1] += 2
    elif command == 'on':
        grid[x_start:x_end+1, y_start:y_end+1] += 1
    elif command == 'off':
        grid[x_start:x_end+1, y_start:y_end+1] -= 1
        grid[x_start:x_end+1, y_start:y_end+1][grid[x_start:x_end+1, y_start:y_end+1]  < 0] = 0

print(f'After following Santa\'s instructions the total brightness of all lights combined is {np.sum(grid):.0f}.')
