from dataclasses import dataclass, field

@dataclass
class Wire:
    path: list[str]
    coordinates: set(tuple((int, int))) = field(init=False)
    steps_to_reach_coordinates: dict[tuple((int, int)), int] = field(init=False)
    
    def __post_init__(self):
        self.coordinates = set()
        self.steps_to_reach_coordinates = dict()
        x = 0
        y = 0
        steps = 0
        
        for instruction in self.path:
            direction = instruction[0]
            num = int(instruction[1:])

            if direction == 'L':
                for _ in range(num):
                    steps += 1
                    x -= 1
                    self.coordinates.add((x, y))
                    if (x, y) not in self.steps_to_reach_coordinates:
                        self.steps_to_reach_coordinates[(x, y)] = steps
            elif direction == 'R':
                for _ in range(num):
                    steps += 1
                    x += 1
                    self.coordinates.add((x, y))
                    if (x, y) not in self.steps_to_reach_coordinates:
                        self.steps_to_reach_coordinates[(x, y)] = steps
            elif direction == 'U':
                for _ in range(num):
                    steps += 1
                    y += 1
                    self.coordinates.add((x, y))
                    if (x, y) not in self.steps_to_reach_coordinates:
                        self.steps_to_reach_coordinates[(x, y)] = steps
            elif direction == 'D':
                for _ in range(num):
                    steps += 1
                    y -= 1
                    self.coordinates.add((x, y))
                    if (x, y) not in self.steps_to_reach_coordinates:
                        self.steps_to_reach_coordinates[(x, y)] = steps
with open('inputs/day03.txt') as f:
    wires = f.read().split('\n')

first_wire  = Wire(wires[0].split(','))
second_wire = Wire(wires[1].split(','))

intersection_coordinates = first_wire.coordinates.intersection(second_wire.coordinates)

min_distance = float('inf')
closest_intersection = None

for coordinate in intersection_coordinates:
    x, y = coordinate
    manhattan_distance = abs(x) + abs(y)
    
    if manhattan_distance < min_distance:
        min_distance = manhattan_distance
        closest_intersection = coordinate

# Part 1 solution.
print(f'The intersection closest to the central port is {closest_intersection} with Manhattan distance {min_distance}.')

min_steps = float('inf')
best_coordinate = None

for coordinate in intersection_coordinates:
    wire_1_steps = first_wire.steps_to_reach_coordinates[coordinate]
    wire_2_steps = second_wire.steps_to_reach_coordinates[coordinate]
    combined_steps = wire_1_steps + wire_2_steps

    if combined_steps < min_steps:
        min_steps = combined_steps
        best_coordinate = coordinate

# Part 2 solution.
print(f'The coordinate with the lowest combined signal delay is {best_coordinate} with combined steps of {min_steps}.')
