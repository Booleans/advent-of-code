import re
from math import lcm

pattern = r'^(?P<node>\w{3}) = \((?P<L>\w{3}), (?P<R>\w{3})\)$'
re_nodes = re.compile(pattern)

with open('inputs/day08.txt') as f:
    raw = f.read().split('\n')
    INSTRUCTIONS = raw[0]
    MAP = raw[2:]

network = dict()

for line in MAP:
    path = re_nodes.match(line).groupdict()
    node = path['node']
    left_node = path['L']
    right_node = path['R']

    network[node] = {'L':left_node, 'R':right_node}

node = 'AAA'
num_instructions = len(INSTRUCTIONS)
count = 0

while node != 'ZZZ':
    instruction = INSTRUCTIONS[count%num_instructions]
    node = network[node][instruction]
    count += 1
else:
    # Part 1 solution.
    print(f'The number of steps to go from node AAA to node ZZZ is {count}.')
    
nodes_ending_in_A = {node for node in network if node[2] == 'A'}
nodes_ending_in_Z = {node for node in network if node[2] == 'Z'}

steps_required_for_A_nodes = []

for node in nodes_ending_in_A:
    count = 0

    while node not in nodes_ending_in_Z:
        instruction = INSTRUCTIONS[count%num_instructions]
        node = network[node][instruction]
        count += 1
    else:
        steps_required_for_A_nodes.append(count)

least_common_multiple = lcm(*steps_required_for_A_nodes)

# Part 2 solution.
print(f'The number of steps required for all A nodes to end in a Z node is {least_common_multiple}')
