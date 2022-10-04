from operator import __and__, __or__, __rshift__, __lshift__, __not__

gate_values = dict()

instructions = "cj OR cp -> cq"

instruction, output_gate = instructions.split("->")

functions = {
    "AND": __and__,
    "OR": __or__,
    "NOT": __not__,
    "LSHIFT": __lshift__,
    "RIGHT": __rshift__,
}

print(instruction, output_gate)
