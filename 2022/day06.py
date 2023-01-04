with open("inputs/day06.txt") as f:
    characters = f.read()

for i, _ in enumerate(characters):
    letters = characters[i:i+4]
    if len(set(letters)) == 4:
        first_marker_position = i + 4
        break
    
for i, _ in enumerate(characters):
    letters = characters[i:i+14]
    if len(set(letters)) == 14:
        start_of_message_marker = i + 14
        break

# Part 1 solution.
print(f'{first_marker_position} characters need to be processed before the first start-of-packet marker is detected.')

# Part 2 solution.
print(f'{start_of_message_marker} characters need to be processed before the first start-of-message marker is detected.')