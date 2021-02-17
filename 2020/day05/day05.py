# FBFBBFF
with open('input.txt') as f:
    boarding_passes = [line.strip() for line in f]

translator = str.maketrans({'F':'0', 'R':'1', 'B':'1', 'L':'0'})

boarding_passes = [seat.translate(translator) for seat in boarding_passes]

highest_ID = 0

for seat in boarding_passes:
    row = int(seat[:7], 2)
    column = int(seat[-3:], 2)
    ID = row * 8 + column
    
    if ID > highest_ID:
        highest_ID = ID
# Part 1 solution.
print(highest_ID)