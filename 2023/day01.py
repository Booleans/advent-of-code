import re

with open("inputs/day01.txt") as f:
    instructions = f.read().split()

pattern = r'(\d)'

digits = re.compile(pattern)

total = 0

for instruction in instructions:
    numbers = digits.findall(instruction)
    total += int(f'{numbers[0]}{numbers[-1]}')

# Part 1 solution.
print(f'The sum of all calibration values is {total}.')

pattern = r'(?=(\d|zero|one|two|three|four|five|six|seven|eight|nine))'

digits = re.compile(pattern)

mapper = {'zero':0, 'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}
total = 0

for instruction in instructions:
    numbers = digits.findall(instruction)
    first = numbers[0]
    last = numbers[-1]

    if first in mapper:
        first = mapper[first]
    if last in mapper:
        last = mapper[last]

    total += int(f'{first}{last}')

# Part 2 solution.
print(f'The sum of all calibration values is {total}.')
