import re

with open("input.txt") as f:
    raw = f.read()

# Passports are separated by '\n\n'.
passports = [passport.replace("\n", " ") for passport in raw.split("\n\n")]


def all_fields_present(passport):
    pattern = "^.*(?=.*byr)(?=.*iyr)(?=.*eyr)(?=.*hgt)(?=.*hcl)(?=.*ecl)(?=.*pid).*$"
    valid = re.compile(pattern)
    return bool(valid.match(pattern, passport))


# Part 1 solution, a passport is valid if all required fields are present.
print(sum(all_fields_present(passport) for passport in passports))


def all_fields_present_and_valid(passport):
    fields = {
        "byr": r"(?=.*byr:(19[2-9][0-9]|200[0-2])\b)",
        "iyr": r"(?=.*iyr:(201[0-9]|2020)\b)",
        "eyr": r"(?=.*eyr:(202[0-9]|2030)\b)",
        "hgt": r"(?=.*hgt:((59|6\d|7[0-6])in|(1[5-8]\d|19[0-3])cm)\b)",
        "hcl": r"(?=.*hcl:#[\d|a-f]{6}\b)",
        "ecl": r"(?=.*ecl:(amb|blu|brn|gry|grn|hzl|oth)\b)",
        "pid": r"(?=.*pid:\d{9}\b)",
    }

    valid_pattern = (
        "^" + "".join([pattern for field, pattern in fields.items()]) + ".*$"
    )
    valid_passport = re.compile(valid_pattern)
    return bool(valid_passport.match(passport))


# Part 2 solution, a passport is valid if all required fields are present and have a valid input.
print(sum(all_fields_present_and_valid(passport) for passport in passports))
