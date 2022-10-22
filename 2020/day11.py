import numpy as np
from scipy.signal import convolve2d

with open("inputs/day11.txt") as f:
    waiting_area = tuple(line.strip() for line in f)

is_seat = np.array(
    [[1 if space != "." else 0 for space in row] for row in waiting_area]
)

seats_occupied = np.array(
    [[1 if space == "#" else 0 for space in row] for row in waiting_area]
)


c = np.ones(shape=(3, 3), dtype=np.int8)
c[1, 1] = 0

while True:
    previous_state = np.copy(seats_occupied)
    adjacent_seats_occupied = np.uint8(convolve2d(seats_occupied, c, mode="same"))
    seats_becoming_occupied = is_seat & (adjacent_seats_occupied == 0)
    seats_becoming_empty = is_seat & (adjacent_seats_occupied >= 4)
    seats_occupied = np.where(seats_becoming_occupied, 1, seats_occupied)
    seats_occupied = np.where(seats_becoming_empty, 0, seats_occupied)

    if np.all(seats_occupied == previous_state):
        break

number_of_seats_occupied = np.sum(seats_occupied)

# Part 1 solution.
print(
    f"When the waiting area has stabilized there are {number_of_seats_occupied} seats occupied."
)
