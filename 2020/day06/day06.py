with open('input.txt') as f:
    raw = f.read()

# Groups are separated by '\n\n'.
groups = [passport.split('\n') for passport in raw.split('\n\n')]

yes_counts_by_group = (len(set(''.join(group))) for group in groups)

# Part 1 solution.
print(sum(yes_counts_by_group))

num_questions_all_answered_yes = []

for group in groups:
    all_yes = set(group[0])
    for person in group:
        all_yes.intersection_update(set(person))
    num_questions_all_answered_yes.append(len(all_yes))

# Part 2 solution.
print(sum(num_questions_all_answered_yes))