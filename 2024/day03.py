import re 

with open("inputs/day03.txt") as f:
    raw = f.read()

pattern = r'mul\((\d{1,3}),(\d{1,3})\)'

total = sum(int(num1) * int(num2) for num1, num2 in re.findall(pattern, raw))

print(f'If you add up the results of all valid multiplications you get {total}.')