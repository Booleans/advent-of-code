class Keypad:
    def __init__(self):
        self.keys: list[list[int]] = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.x = 1
        self.y = 1

    def get_key(self, instruction: str):
        for direction in instruction:
            if direction == "U" and self.x > 0:
                self.x -= 1
            elif direction == "D" and self.x < 2:
                self.x += 1
            elif direction == "L" and self.y > 0:
                self.y -= 1
            elif direction == "R" and self.y < 2:
                self.y += 1

        return self.keys[self.x][self.y]


with open("inputs/day02.txt") as f:
    instructions = f.read().split("\n")

keypad = Keypad()

nums = [keypad.get_key(instruction) for instruction in instructions]

# Part 1 solution.
print(f"The bathroom code is {nums}.")
