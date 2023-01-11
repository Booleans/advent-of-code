from string import ascii_letters

with open("inputs/day03.txt") as f:
    rucksacks = f.read().split("\n")

priorities = {letter: i + 1 for i, letter in enumerate(ascii_letters)}
total_priority = 0

for rucksack in rucksacks:
    midpoint = len(rucksack) // 2
    first_compartment = set(rucksack[:midpoint])
    second_compartment = set(rucksack[midpoint:])

    overlapping_item = first_compartment.intersection(second_compartment).pop()
    total_priority += priorities[overlapping_item]

# Part 1 solution.
print(
    f"The sum of priorities of overlapping items in each rucksack is {total_priority}."
)

total_priority = 0

for i in range(0, len(rucksacks), 3):
    rucksack1 = set(rucksacks[i])
    rucksack2 = set(rucksacks[i + 1])
    rucksack3 = set(rucksacks[i + 2])

    overlapping_item = rucksack1.intersection(rucksack2).intersection(rucksack3).pop()
    total_priority += priorities[overlapping_item]

# Part 2 solution.
print(
    f"The sum of priorities of overlapping items in each group's rucksack is {total_priority}."
)
