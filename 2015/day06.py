"""
Example lines of input:
turn on 0,0 through 999,999 would turn on (or leave on) every light.
toggle 0,0 through 999,0 would toggle the first line of 1000 lights, turning off the ones that were on, and turning on the ones that were off.
turn off 499,499 through 500,500 would turn off (or leave off) the middle four lights.
"""

import numpy as np
import re

with open("inputs/day06.txt") as f:
    instructions = tuple(line.strip() for line in f)

grid = np.zeros(shape=(1000, 1000))

for instruction in instructions:
    command = re.search(r"toggle|on|off", instruction).group()
    matches = [int(match) for match in re.findall(r"(\d{1,3})", instruction)]
    x_start, y_start, x_end, y_end = matches

    if command == "toggle":
        grid[x_start : x_end + 1, y_start : y_end + 1] = np.logical_not(
            grid[x_start : x_end + 1, y_start : y_end + 1]
        )
    elif command == "on":
        grid[x_start : x_end + 1, y_start : y_end + 1] = 1
    elif command == "off":
        grid[x_start : x_end + 1, y_start : y_end + 1] = 0

print(f"After following the instructions {np.sum(grid):.0f} lights are lit.")

grid = np.zeros(shape=(1000, 1000))

for instruction in instructions:
    command = re.search(r"toggle|on|off", instruction).group()
    matches = [int(match) for match in re.findall(r"(\d{1,3})", instruction)]
    x_start, y_start, x_end, y_end = matches

    if command == "toggle":
        grid[x_start : x_end + 1, y_start : y_end + 1] += 2
    elif command == "on":
        grid[x_start : x_end + 1, y_start : y_end + 1] += 1
    elif command == "off":
        grid[x_start : x_end + 1, y_start : y_end + 1] -= 1
        grid[x_start : x_end + 1, y_start : y_end + 1][
            grid[x_start : x_end + 1, y_start : y_end + 1] < 0
        ] = 0

print(
    f"After following Santa's instructions the total brightness of all lights combined is {np.sum(grid):.0f}."
)
