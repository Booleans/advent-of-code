import re

with open('input.txt') as f:
    RULES = tuple(line.strip() for line in f)
    
parent_bag_pattern = r'^(\w+ \w+) (?:bags.+)$'
child_bag_pattern = r'(\d \w+ \w+)'

bags_inside_this = dict()
bags_containing_this = dict()

for rule in RULES:
    parent_color = re.findall(parent_bag_pattern, rule)[0]
    bags_inside_this[parent_color] = dict()
    
    bags_inside = re.findall(child_bag_pattern, rule)
    
    for bag in bags_inside:
        number = int(bag[:2])
        color = bag[2:]

        bags_inside_this[parent_color][color] = number
        
        if color in bags_containing_this:
            bags_containing_this[color].add(parent_color)
        else:
            bags_containing_this[color] = set([parent_color])

can_contain_gold = set()

searching = ['shiny gold']

while searching:
    current_color = searching.pop()

    if current_color in bags_containing_this:
        parent_bags = bags_containing_this[current_color]

        for bag in parent_bags:
            if bag not in can_contain_gold:
                searching.append(bag)
                can_contain_gold.add(bag)

# Part 1 solution.                
print(len(can_contain_gold))

bag_counts = 0
searching = ['shiny gold']

while searching:
    current_color = searching.pop()
    if current_color in bags_inside_this:
        bags_inside = bags_inside_this[current_color]
        
        for bag, count in bags_inside.items():
            bag_counts += count
            for _ in range(count):
                searching.append(bag)
# Part 2 solution.            
print(bag_counts)