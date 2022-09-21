from dataclasses import dataclass, field

@dataclass
class Rectangle:
    claim: str
    ID: str = field(init=False)
    inches_from_left: int = field(init=False)
    inches_from_top: int = field(init=False)
    width: int = field(init=False)
    height: int = field(init=False)
    x_min: int = field(init=False)
    x_max: int = field(init=False)
    y_min: int = field(init=False)
    y_max: int = field(init=False)
    
    def __post_init__(self):
        claim_components = self.claim.split()
        self.ID = claim_components[0]
        inches_from_left, inches_from_top = claim_components[2][:-1].split(',')
        self.inches_from_left = int(inches_from_left)
        self.inches_from_top = int(inches_from_top)
        width, height = claim_components[3].split('x')
        self.width = int(width)
        self.height = int(height)
        self.x_min = self.inches_from_left
        self.x_max = self.x_min + self.width
        self.y_min = self.inches_from_top
        self.y_max = self.y_min + self.height

with open('inputs/day03.txt') as f:
    rectangles = [Rectangle(line) for line in f.read().split('\n')]

coordinates_occupied = set()
overlapping_coordinates = set()

for rectangle in rectangles:
    for x in range(rectangle.x_min, rectangle.x_max):
        for y in range(rectangle.y_min, rectangle.y_max):
            coordinate = (x, y)
            if coordinate in coordinates_occupied:
                overlapping_coordinates.add(coordinate)
            else:
                coordinates_occupied.add(coordinate)

# Part 1 solution.
print(f'There are {len(overlapping_coordinates)} square inches that have overlapping claims.')