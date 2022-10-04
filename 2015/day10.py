starting_num = "3113322113"


class Sequence:
    def __init__(self, num: str):
        self.num = num
        self.length = len(num)

    def next_sequence(self):
        current_digit = self.num[0]
        count = 0
        new_num = ""

        for digit in self.num:
            if digit == current_digit:
                count += 1
            else:
                new_num += f"{count}{current_digit}"
                count = 1
                current_digit = digit
        else:
            new_num += f"{count}{current_digit}"

        self.num = new_num
        self.length = len(self.num)


sequence = Sequence(starting_num)

for _ in range(40):
    sequence.next_sequence()

# Part 1 solution.
print(f"After 40 iterations the length is {sequence.length} digits.")

for _ in range(10):
    sequence.next_sequence()

# Part 2 solution.
print(f"After 50 iterations the length is {sequence.length} digits.")
