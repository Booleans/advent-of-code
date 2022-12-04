from dataclasses import dataclass, field

@dataclass
class RPSGame:
    strategy: str
    opponent_choice: str = field(init=False)
    my_choice: str = field(init=False)
    result: str = field(init=False)
    score: int = field(init=False)
    
    def __post_init__(self):
        choice_mapper = {'A':'rock', 'B':'paper', 'C':'scissors', 'X':'rock', 'Y':'paper', 'Z':'scissors'}
        points_for_result = {'loss':0, 'draw':3, 'win':6}
        points_for_choice = {'rock':1, 'paper':2, 'scissors':3}
        choice_values = {'rock':0, 'paper':1, 'scissors':2}
        
        self.opponent_choice = choice_mapper[self.strategy[0]]
        self.my_choice = choice_mapper[self.strategy[-1]]
        
        winner = (3 + choice_values[self.my_choice] - choice_values[self.opponent_choice]) % 3
        
        if winner == 1:
            self.result = 'win'
        elif winner == 2:
            self.result = 'loss'
        else:
            self.result = 'draw'
            
        self.score = points_for_choice[self.my_choice] + points_for_result[self.result]

with open("inputs/day02.txt") as f:
    games = [RPSGame(line) for line in f.read().split('\n')]

total_score = sum(game.score for game in games)

# Part 1 solution.
print(f'My total score, if I follow the strategy guide, would be {total_score} points.')