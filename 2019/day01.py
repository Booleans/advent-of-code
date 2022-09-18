from dataclasses import dataclass, field

@dataclass
class Spaceship:
    mass: int
    fuel_for_mass: int = field(init=False)
    fuel_for_fuel: int = field(init=False)
    fuel_total:    int = field(init=False)

    def __post_init__(self):
        self.fuel_for_mass = self.mass//3 - 2
        self.fuel_for_fuel = 0
        fuel_added = self.fuel_for_mass
        while fuel_added > 0:
            additional_fuel_needed = fuel_added//3 - 2
            fuel_added = additional_fuel_needed
            if additional_fuel_needed > 0:
                self.fuel_for_fuel += additional_fuel_needed
        
        self.fuel_total = self.fuel_for_mass + self.fuel_for_fuel

with open('inputs/day01.txt') as f:
    spaceships = [Spaceship(int(line.strip())) for line in f]

# Part 1 solution. 
print(sum(ship.fuel_for_mass for ship in spaceships))

# Part 2 solution. 
print(sum(ship.fuel_total for ship in spaceships))