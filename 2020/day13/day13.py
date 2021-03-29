from math import ceil

start_time = 1000066
busses = '13,x,x,41,x,x,x,37,x,x,x,x,x,659,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,19,x,x,x,23,x,x,x,x,x,29,x,409,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,17'

bus_numbers = [int(number) for number in busses.split(',') if number != 'x']

next_arrival = []
closest_bus = None
closest_arrival = float('inf')

for number in bus_numbers:
    next_arrival_time = ceil(start_time/number)*number
    
    if next_arrival_time < closest_arrival:
        closest_arrival = next_arrival_time
        closest_bus = number

time_waited = closest_arrival - start_time
# Part 1 solution.
print(time_waited * closest_bus)

# Now we need both the bus number and index position.
bus_numbers = [(i, int(number)) for i, number in enumerate(busses.split(',')) if number != 'x']

num = 13*19*23*29*659 # 108569591

while not all((
(num - 10) % 41 == 0,
(num - 6)  % 37 == 0,
(num + 31) % 409 == 0,
(num + 48) % 17 == 0,
)):
    num += 108569591

# Part 2 solution.
print(num - 13)
