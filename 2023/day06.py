from math import ceil, floor, sqrt
import re

def num_ways_to_win(TIME, DISTANCE):
    # Quadratic formula.
    max_holding_time = floor((TIME + sqrt(TIME**2 - 4*DISTANCE))/2) 
    min_holding_time = ceil((TIME - sqrt(TIME**2 - 4*DISTANCE))/2) 

    return len(range(min_holding_time, max_holding_time+1))


with open('inputs/day06.txt') as f:
    times, distances = f.read().split('\n')

pattern = f'(\d+)'
numbers = re.compile(pattern)

race_times = tuple(int(time) for time in numbers.findall(times))
race_distances = tuple(int(time) for time in numbers.findall(distances))

total = 1

for time, distance in zip(race_times, race_distances):
    total *= num_ways_to_win(time, distance)

# Part 1 solution.
print(f'If you multiply together the number of ways to win each race you get {total}.')

single_race_time = int(''.join(str(time) for time in race_times))
single_race_distance = int(''.join(str(time) for time in race_distances))

ways_to_win = num_ways_to_win(single_race_time, single_race_distance)

# Part 2 solution.
print(f'There are {ways_to_win} ways to win this single race.')
