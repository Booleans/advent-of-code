with open("inputs/day01.txt") as f:
    digits = [int(digit) for digit in f.read()]

# Part 1 solution.
# Instead of checking for a matching digit 1 ahead of the current digit, we check 1 behind.
# This means that index 0 checks index -1, which is what we need to check if the first digit and last digit match.
print(sum(digit for i, digit in enumerate(digits) if digit == digits[i - 1]))

# Part 2 solution.
half_size_of_list = int(len(digits) / 2)
print(
    sum(
        digit
        for i, digit in enumerate(digits)
        if digit == digits[i - half_size_of_list]
    )
)
