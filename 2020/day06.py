from dataclasses import dataclass, field

@dataclass
class Group:
    responses: list[str]
    questions_any_answered_yes: set[str] = field(init=False)
    questions_all_answered_yes: set[str] = field(init=False)

    def __post_init__(self):
        self.questions_any_answered_yes = set()
        self.questions_all_answered_yes = set(self.responses[0])
        
        for person in self.responses:
            self.questions_any_answered_yes.update(person)
            self.questions_all_answered_yes.intersection_update(person)

with open('inputs/day06.txt') as f:
    raw = f.read()

# Groups are separated by '\n\n'.
groups = [Group(passport.split('\n')) for passport in raw.split('\n\n')]

# Part 1 solution.
print(sum(len(group.questions_any_answered_yes) for group in groups))

# Part 2 solution.
print(sum(len(group.questions_all_answered_yes) for group in groups))
