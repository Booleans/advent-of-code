import re
from dataclasses import dataclass, field
from collections import defaultdict
from operator import ge, gt, le, lt, add, sub, eq, ne

pattern = r"^(\w+) (dec|inc) (-?\d+) if (\w+) (<|<=|==|!=|>|>=) (-?\d+)$"

direction_mapper = {"dec": sub, "inc": add}
operation_mapper = {">=": ge, ">": gt, "==": eq, "!=": ne, "<=": le, "<": lt}


@dataclass
class Instruction:
    target: str
    direction: any
    amount: int
    condition_register: str
    condition_check: any
    condition_value: int

    def __post_init__(self):
        self.direction = direction_mapper[self.direction]
        self.amount = int(self.amount)
        self.condition_value = int(self.condition_value)
        self.condition_check = operation_mapper[self.condition_check]


def parse(raw: str) -> list[Instruction]:
    lines = raw.split("\n")
    relevant_instructions = [re.match(pattern, line).groups() for line in lines]
    return [Instruction(*instruction) for instruction in relevant_instructions]


with open("inputs/day08.txt") as f:
    INSTRUCTIONS = parse(f.read())

register_values = defaultdict(int)

highest_value_held = 0

for instruction in INSTRUCTIONS:
    check_value = register_values[instruction.condition_register]
    condition_met = instruction.condition_check(
        check_value, instruction.condition_value
    )

    if condition_met:
        register_values[instruction.target] = instruction.direction(
            register_values[instruction.target], instruction.amount
        )
        highest_value_held = max(
            highest_value_held, register_values[instruction.target]
        )

print(
    f"The largest value in any register after completing the instructions is {max(register_values.values())}."
)
print(
    f"The highest value held in any register during the process is {highest_value_held}."
)
