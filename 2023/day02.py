from dataclasses import dataclass
import re

# TODO: Make a better regex pattern instead of separate patterns for each color.
reds = re.compile(f'(\d+) red')
greens = re.compile(f'(\d+) green')
blues = re.compile(f'(\d+) blue')

@dataclass
class Game:
    id: int
    games: list[str]
    max_blue: int = 0
    max_green: int = 0
    max_red: int = 0

    def __post_init__(self):
        global reds
        global greens
        global blues

        games = self.games.split(';')
        for game in games:
            if reds.findall(game):
                num_reds = int(reds.findall(game)[0])
                self.max_red = max(self.max_red, num_reds)
            if blues.findall(game):
                num_blues = int(blues.findall(game)[0])
                self.max_blue = max(self.max_blue, num_blues)
            if greens.findall(game):
                num_greens = int(greens.findall(game)[0])
                self.max_green = max(self.max_green, num_greens)

with open("inputs/day02.txt") as f:
    GAMES = f.read().split('\n')

games = []
for game in GAMES:
    game_info, colors = game.split(':')
    game_id = int(game_info.split(' ')[1])
    games.append(Game(game_id, colors.strip()))

possible_games = [game for game in games if game.max_blue <= 14 and game.max_green <= 13 and game.max_red <= 12]

# Part 1 solution. 
print(f'The sum of the IDs of possible games is {sum(game.id for game in possible_games)}.')

power_sets = (game.max_blue * game.max_red * game.max_green for game in games)
# Part 2 solution. 
print(f'The sum of the power sets is {sum(power_sets)}.')
