with open("inputs/day01.txt") as f:
    elf_inventories = f.read().split("\n\n")
    elf_inventories = [
        [int(snack) for snack in elf.split("\n")] for elf in elf_inventories
    ]

calories_carried = sorted([sum(elf) for elf in elf_inventories], reverse=True)

# Part 1 solution.
print(f"The elf carrying the most calories is carrying {calories_carried[0]} calories.")

# Part 2 solution.
print(f"The top three elves are carrying {sum(calories_carried[:3])} calories.")
