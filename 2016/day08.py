from dataclasses import dataclass, field
import numpy as np


@dataclass
class Instruction:
    raw: str

width = 5
height = 6
screen = np.zeros(shape=(height, width))

# rect 3x2
screen[:2, :3] = 1
print(screen)

# rotate column x=1 by 1
rotations = 0
col = 1
net_rotations = rotations % height

screen[:, col] = np.concatenate((screen[-net_rotations:, col], screen[:-net_rotations, col]))

rotations = 1
row = 0
net_rotations = rotations % width

screen[row, :] = np.concatenate((screen[row, -net_rotations:], screen[row, :-net_rotations]))

print(screen)