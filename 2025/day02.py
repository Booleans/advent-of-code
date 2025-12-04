import re 

pattern = r'^(\d+)\1$'

invalid_ID = re.compile(pattern)

invalid_IDs = [] 

with open("inputs/day02.txt") as f:
    raw = f.read().split(',')
    product_ID_ranges = []
    for id_range in raw:
        start_num, stop_num = id_range.split('-')
        product_ID_ranges.append(range(int(start_num), int(stop_num)+1))

for ID_range in product_ID_ranges:
    for num in ID_range:
        if invalid_ID.match(str(num)):
            invalid_IDs.append(num)

print(sum(invalid_IDs))