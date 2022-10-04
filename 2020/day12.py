with open("inputs/day12.txt") as f:
    INSTRUCTIONS = tuple(line.strip() for line in f)

facing = "E"

turns = {
    "R": {"N": "E", "S": "W", "E": "S", "W": "N"},
    "L": {"N": "W", "S": "E", "E": "N", "W": "S"},
}

position_x = 0
position_y = 0

for instruction in INSTRUCTIONS:
    direction, number = instruction[0], int(instruction[1:])

    if direction in ("R", "L"):
        number //= 90
        for _ in range(number):
            facing = turns[direction][facing]
        continue

    if direction == "F":
        direction = facing

    if direction == "N":
        position_y += number
    elif direction == "S":
        position_y -= number
    elif direction == "E":
        position_x += number
    elif direction == "W":
        position_x -= number

manhattan_distance = abs(position_x) + abs(position_y)
print(manhattan_distance)
