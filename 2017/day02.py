with open("inputs/day02.txt") as f:
    rows = [line.split("\t") for line in f.read().split("\n")]
    spreadsheet = [sorted([int(num) for num in row]) for row in rows]

max_min_difference = (max(row) - min(row) for row in spreadsheet)
checksum = sum(max_min_difference)

# Part 1 solution.
print(f"The checksum of the spreadsheet is {checksum}.")

evenly_divided_numbers = []

for row in spreadsheet:
    for i, lower_num in enumerate(row):
        for higher_num in row[i + 1 :]:
            if higher_num % lower_num == 0:
                evenly_divided_numbers.append((higher_num, lower_num))
                break

sum_divided_numbers = sum(
    int(high_num / low_num) for high_num, low_num in evenly_divided_numbers
)

print(f"The sum of dividing the evenly divided numbers is {sum_divided_numbers}.")
