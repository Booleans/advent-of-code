import re

pattern = r"^\d*(\d)\1\d*$"

repeating_adjacent_digit = re.compile(pattern)
passwords = [str(num) for num in range(193651, 649730)]

valid_passwords = [
    password
    for password in passwords
    if "".join(sorted(password)) == password
    and repeating_adjacent_digit.match(password)
]

# Part 1 solution.
print(f"There are {len(valid_passwords)} potential passwords that meet the criteria.")

# Create a regex pattern for each of the digits 1-9.
# Digit must appear 2 times sequentially but then not have that same digit present to the left or right.
patterns = [rf"[^{num}|\b]*{num}{num}[^{num}|\b]*$" for num in range(1, 10)]
# Combine the patterns together separated by |
# This forms one large pattern that says "match if a 1 appears exactly twice, or a 2 exactly twice, or a 3..."
pattern = "|".join(patterns)
print(pattern)
password_match = re.compile(pattern)

valid_under_stricter_rules = [
    password for password in valid_passwords if password_match.match(password)
]
num_valid_password = len(valid_under_stricter_rules)

# Part 2 solution.
print(f"There are {num_valid_password} valid passwords under the stricter criteria.")
