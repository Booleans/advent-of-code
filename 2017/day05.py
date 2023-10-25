with open("inputs/day05.txt") as f:
    JUMPS = [int(digit) for digit in f.read().split("\n")]

steps_taken = 0
i = 0

jumps = [num for num in JUMPS]

while i in range(len(jumps)):
    jump = jumps[i]
    jumps[i] += 1
    i += jump
    steps_taken += 1
else:
    print(steps_taken)


steps_taken = 0
i = 0

jumps = [num for num in JUMPS]

while i in range(len(jumps)):
    jump = jumps[i]
    if jump >= 3:
        jumps[i] -= 1
    else:
        jumps[i] += 1
    i += jump
    steps_taken += 1
else:
    print(steps_taken)
