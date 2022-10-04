def count_tree_hits(forest, slope=(3, 1)):
    right = slope[0]
    down = slope[1]
    length = len(forest)
    width = len(forest[0])

    x = 0
    trees = 0

    for y in range(0, length, down):
        trees += forest[y][x]
        x += right
        x = x % width

    return trees


with open("inputs/day03.txt") as f:
    forest = [line.strip() for line in f]

# Let's make our forest 1s and 0s, with a 1 representing a tree.
# This makes it slightly easier to take the sum of tree encounters.
forest = [[1 if char == "#" else 0 for char in row] for row in forest]

# Part 1
print(count_tree_hits(forest, (3, 1)))

# Part 2
SLOPES = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

product = 1

for slope in SLOPES:
    product *= count_tree_hits(forest, slope)

print(product)
