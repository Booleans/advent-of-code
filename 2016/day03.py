from dataclasses import dataclass, field


@dataclass
class Triangle:
    sides: list[int]
    small_side: int = field(init=False)
    medium_side: int = field(init=False)
    large_side: int = field(init=False)
    is_valid: bool = field(init=False)

    def __post_init__(self):
        sorted_sides = sorted(self.sides)
        self.small_side = sorted_sides[0]
        self.medium_side = sorted_sides[1]
        self.large_side = sorted_sides[2]
        self.is_possible = (self.small_side + self.medium_side) > self.large_side


with open("inputs/day03.txt") as f:
    rows = [row.strip() for row in f.read().split("\n")]
    rows = [row.split(" ") for row in rows]
    rows = [[int(item) for item in row if item != ""] for row in rows]


triangles = [Triangle(row) for row in rows]

# Part 1 solution.
num_valid_triangles = sum(triangle.is_possible for triangle in triangles)
print(f"There are {num_valid_triangles} possible triangles.")

col0 = sorted([row[0] for row in rows])
col1 = sorted([row[1] for row in rows])
col2 = sorted([row[2] for row in rows])

print(col1)
