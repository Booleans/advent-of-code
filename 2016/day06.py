from collections import Counter

with open("inputs/day06.txt") as f:
    messages = f.read().split("\n")

column_letter_count = dict()

for i, letter in enumerate(messages[0]):
    column_letter_count[i] = Counter()

for message in messages:
    for i, letter in enumerate(message):
        column_letter_count[i][letter] += 1

most_common_letters = "".join(
    [column.most_common(1)[0][0] for column in column_letter_count.values()]
)

# Part 1 solution.
print(f"The error-corrected message is {most_common_letters}.")

least_common_letters = "".join(
    [column.most_common()[::-1][0][0] for column in column_letter_count.values()]
)

print(f"Using the new methodology, the original message is {least_common_letters}.")
