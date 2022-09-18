with open('inputs/day06.txt') as f:
    ORBITS = tuple(line.strip() for line in f)

orbits = {'COM':None}

for orbit in ORBITS:
    orbiting, space_object = orbit.split(')')
    orbits[space_object] = orbiting

num_orbits = 0
for space_object in orbits:
    while space_object != 'COM':
        num_orbits += 1
        space_object = orbits[space_object]

# Part 1 solution. 
print(f'The total number of direct and indirect orbits is {num_orbits}.')