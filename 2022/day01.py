from dataclasses import dataclass, field


@dataclass
class Elf:
    foods: list[int]
    calories: int = field(init=False)

    def __post_init__(self):
        self.calories = sum(self.foods)


def parse(raw: str) -> list[Elf]:
    return [Elf([int(food) for food in line.split("\n")]) for line in raw.split("\n\n")]


with open("inputs/day01.txt") as f:
    elves = parse(f.read())

calories_carried = sorted([elf.calories for elf in elves], reverse=True)

# Part 1 solution.
print(f"The elf carrying the most calories is carrying {calories_carried[0]} calories.")

# Part 2 solution.
print(f"The top three elves are carrying {sum(calories_carried[:3])} calories.")
