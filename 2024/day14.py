import re

class Robot:
    def __init__(self, x, y, velocity_x, velocity_y):
        self.x = x
        self.y = y
        self.velocity_x = velocity_x
        self.velocity_y = velocity_y

    def move(self, n_seconds=1):
        # Define a positive move in the x direction as to the right.
        # And a positive move in the y direction is down. 
        # The grid is 101 tiles wide and 103 tiles tall. 
        moves_right = n_seconds * self.velocity_x
        moves_down = n_seconds * self.velocity_y
        self.x = (self.x + moves_right) % 101
        self.y = (self.x + moves_down) % 103

class EasterBunnyHQ:
    def __init__(self, robots):
        self.robots = robots
        self.quandrant_1_x_range = range(0, 50)
        self.quandrant_1_y_range = range(0, 57)
        self.quandrant_2_x_range = range(51, 101)
        self.quandrant_2_y_range = range(0, 57)
        self.quandrant_3_x_range = range(0, 50)
        self.quandrant_3_y_range = range(57, 103)
        self.quandrant_4_x_range = range(51, 101)
        self.quandrant_4_y_range = range(57, 103)
    
    def move_robots(self, n_seconds=1):
        for robot in self.robots:
            robot.move(n_seconds=n_seconds)

pattern = r'(-?\d+)'
robot_inputs = re.compile(pattern=pattern)

robots = [] 

with open("inputs/day14.txt") as f:
    lines = f.read().split('\n')
    for line in lines:
        inputs = robot_inputs.findall(line)
        inputs = tuple(int(num) for num in inputs)
        robots.append(Robot(*inputs))


EBHQ = EasterBunnyHQ(robots)
EBHQ.move_robots(100)
q1 = 0
q2 = 0
q3 = 0
q4 = 0


for robot in EBHQ.robots:
    if robot.x in EBHQ.quandrant_1_x_range and robot.y in EBHQ.quandrant_1_y_range:
        q1 += 1
    elif robot.x in EBHQ.quandrant_2_x_range and robot.y in EBHQ.quandrant_2_y_range:
        q2 += 1
    elif robot.x in EBHQ.quandrant_3_x_range and robot.y in EBHQ.quandrant_3_y_range:
        q3 += 1
    elif robot.x in EBHQ.quandrant_4_x_range and robot.y in EBHQ.quandrant_4_y_range:
        q4 += 1

safety_score = q1*q2*q3*q4
safety_score