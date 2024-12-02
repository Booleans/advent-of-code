with open("inputs/day02.txt") as f:
    lines = f.read().split('\n')


reports = [line.split() for line in lines]
reports = [[int(num) for num in report] for report in reports]

valid_reports = 0

for report in reports:
    diffs = tuple(first - second for first, second in zip(report[0:], report[1:]))
    valid_reports += all(diff in range(1, 4) for diff in diffs) or all(diff in range(-3, 0) for diff in diffs)

print(f'There are {valid_reports} currently valid reports.')