from dataclasses import dataclass, field


@dataclass
class Line:
    description: str
    x_start: int = field(init=False)
    x_end: int = field(init=False)
    y_start: int = field(init=False)
    y_end: int = field(init=False)
    is_vertical_or_horizontal: bool = field(init=False)

    def __post_init__(self):
        start, end = self.description.strip().split(" -> ")
        x_start, y_start = start.split(",")
        x_end, y_end = end.split(",")
        self.x_start = int(x_start)
        self.y_start = int(y_start)
        self.x_end = int(x_end)
        self.y_end = int(y_end)
        self.is_vertical_or_horizontal = (
            self.x_start == self.x_end or self.y_start == self.y_end
        )


@dataclass
class Grid:
    lines: list[Line]
    coordinates_occupied: set(tuple((int, int))) = field(init=False)
    overlapping_coordinates: set(tuple((int, int))) = field(init=False)

    def __post_init__(self):
        self.coordinates_occupied = set()
        self.overlapping_coordinates = set()

        for line in self.lines:
            for x in range(line.x_start, line.x_end + 1):
                for y in range(line.y_start, line.y_end + 1):
                    coordinate = (x, y)
                    if coordinate in self.coordinates_occupied:
                        self.overlapping_coordinates.add(coordinate)
                    else:
                        self.coordinates_occupied.add(coordinate)


with open("../inputs/day05.txt") as f:
    descriptions = f.read().split("\n")

lines = [Line(description) for description in descriptions]

straight_lines = [line for line in lines if line.is_vertical_or_horizontal]

grid = Grid(straight_lines)

print(len(grid.overlapping_coordinates))
