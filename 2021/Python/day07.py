from statistics import median
import numpy as np

with open("../inputs/day07.txt") as f:
    crabs = [int(position) for position in f.read().split(",")]

crab_positions = np.array(crabs)

median_position = np.median(crab_positions)
fuel_required = np.sum(np.abs(crab_positions - median_position))

# Part 1 solution.
print(fuel_required)


def get_fuel_consumption(proposed_position, positions):
    steps_required = np.abs(positions - proposed_position)
    fuel_required_to_reach_proposed_position = (
        steps_required * (steps_required + 1)
    ) / 2
    total_fuel = np.sum(fuel_required_to_reach_proposed_position)

    return total_fuel


min_position = min(crab_positions)
max_position = max(crab_positions)

possible_positions = range(min_position, max_position + 1)

lowest_fuel_consumption = float("inf")
for position in possible_positions:
    fuel_required = get_fuel_consumption(position, crab_positions)
    if fuel_required < lowest_fuel_consumption:
        lowest_fuel_consumption = fuel_required
    else:
        # Part 2 solution.
        print(lowest_fuel_consumption)
        break
