from dataclasses import dataclass
from string import ascii_uppercase as letters
import re

moves_regex = re.compile(r'move (\d+) from (\d+) to (\d+)')

@dataclass
class Move:
    quantity: int
    from_: int
    to: int
    
with open("inputs/day05.txt") as f:
    raw_crates, raw_moves = f.read().split('\n\n')

stacked_crates = raw_crates.split('\n')

instructions = moves_regex.findall(raw_moves)
instructions = tuple((int(num) for num in instruction) for instruction in instructions)

num_stacks = len(stacked_crates[-1].split())
stacks = {i:list() for i in range(1, num_stacks+1)}

for row in stacked_crates[-2::-1]:
    for i, char in enumerate(row):
        if char in letters:
            stack_num = i//4 + 1
            stacks[stack_num].append(char)

moves = [Move(*instruction) for instruction in instructions]

for move in moves:
    num_moves = min(move.quantity, len(stacks[move.from_]))
    for _ in range(num_moves):
        stacks[move.to].append(stacks[move.from_].pop())

print(''.join(letters[-1] for letters in stacks.values()))