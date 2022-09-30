from collections import Counter

with open("../inputs/day06.txt") as f:
    fish = [int(fish) for fish in f.read().split(",")]

days_to_simulate = 256
fish_counts = Counter(fish)

for days in range(days_to_simulate):
    temp_counter = Counter(fish_counts)
    for timer in range(0, 8):
        temp_counter[timer] = fish_counts[timer + 1]

    temp_counter[8] = fish_counts[0]
    temp_counter[6] += fish_counts[0]

    fish_counts = Counter(temp_counter)

    if days == 80:
        fish_after_80_days = sum(fish_counts.values())

fish_after_256_days = sum(fish_counts.values())

# Part 1 solution.
print(f"After 80 days there are {fish_after_80_days} lanternfish.")

# Part 2 solution.
print(f"After 256 days there are {fish_after_256_days} lanternfish.")
