with open('inputs/day01.txt') as f:
    instructions = f.read().replace(',', '').split(' ')

facing = 'North'

new_direction = {'North':{'R':'East', 'L':'West'},
                 'South':{'R':'West', 'L':'East'},
                 'East': {'R':'South','L':'North'},
                 'West': {'R':'North','L':'South'}}

x_position = 0
y_position = 0

for instruction in instructions:
    turn = instruction[0]
    steps = int(instruction[1:])

    facing = new_direction[facing][turn]

    if facing == 'North':
        y_position += steps
    elif facing == 'South':
        y_position -= steps
    elif facing == 'East':
        x_position += steps
    elif facing == 'West':
        x_position -= steps

blocks_away = abs(x_position) + abs(y_position)

# Part 1 solution.
print(f'The Easter Bunny headquarters is {blocks_away} blocks away.')