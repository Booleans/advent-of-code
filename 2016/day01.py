with open('inputs/day01.txt') as f:
    instructions = f.read().replace(',', '').split(' ')

facing = 'North'

new_direction = {'North':{'R':'East', 'L':'West'},
                 'South':{'R':'West', 'L':'East'},
                 'East': {'R':'South','L':'North'},
                 'West': {'R':'North','L':'South'}}

x_position = 0
y_position = 0
coordinates_visited = set()
first_coordinate_visited_twice = None

for instruction in instructions:
    turn = instruction[0]
    steps = int(instruction[1:])

    facing = new_direction[facing][turn]

    if facing == 'North':
        for _ in range(steps)
        y_position += 1
    elif facing == 'South':
        y_position -= steps
    elif facing == 'East':
        x_position += steps
    elif facing == 'West':
        x_position -= steps

    coordinate = (x_position, y_position)

    if first_coordinate_visited_twice == None and coordinate in coordinates_visited:
        first_coordinate_visited_twice = coordinate
    else:
        coordinates_visited.add(coordinate)

blocks_away = abs(x_position) + abs(y_position)

# Part 1 solution.
print(f'The Easter Bunny headquarters is {blocks_away} blocks away.')

# Part 2 solution.
print(f'The Easter Bunny headquarters is {first_coordinate_visited_twice} blocks away.')