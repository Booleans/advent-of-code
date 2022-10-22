with open("inputs/day10.txt") as f:
    adapters = [int(line.strip()) for line in f]

adapters.sort()
# The aparters are sorted from low to high so instead of calling the max function we can just grab the last element.
final_joltage = adapters[-1] + 3

joltage_difference_count = dict()
joltage_difference_count[1] = 0
joltage_difference_count[3] = 0

current_joltage = 0

for adapter in adapters:
    difference = adapter - current_joltage
    joltage_difference_count[difference] += 1
    current_joltage = adapter
else:
    difference = final_joltage - current_joltage
    joltage_difference_count[difference] += 1

print(joltage_difference_count)
