from collections import Counter

with open("inputs/day02.txt") as f:
    inputs = [line.strip().split() for line in f]

valid_passwords = 0

for line in inputs:
    low, high = line[0].split("-")
    low = int(low)
    high = int(high)
    char = line[1][0]
    password = line[2]

    if low <= Counter(password)[char] <= high:
        valid_passwords += 1

print(valid_passwords)

valid_passwords = 0

for line in inputs:
    low, high = line[0].split("-")
    low = int(low)
    high = int(high)
    char = line[1][0]
    password = line[2]

    if (password[low - 1] == char) != (password[high - 1] == char):
        valid_passwords += 1

print(valid_passwords)
