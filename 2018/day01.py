with open('inputs/day01.txt') as f:
    frequency_changes = tuple(line.strip() for line in f)

current_frequency = 0
frequencies_seen = set()
first_seen_twice = None
frequency_after_first_run = None

while first_seen_twice == None:
    for change in frequency_changes:
        symbol = change[0]
        magnitude = int(change[1:])

        if symbol == '-':
            current_frequency -= magnitude
        elif symbol == '+':
            current_frequency += magnitude
        else:
            print('Invalid symbol detected.')

        if current_frequency in frequencies_seen:
            first_seen_twice = current_frequency
            break
        else:
            frequencies_seen.add(current_frequency)
    
    if frequency_after_first_run == None:
        frequency_after_first_run = current_frequency

# Part 1 solution.
print(f'At the end of the first run the frequency is {frequency_after_first_run}.')

# Part 2 solution.
print(f'Looping the changes until we see a repeated frequency the first repeated frequency is {first_seen_twice}.')
