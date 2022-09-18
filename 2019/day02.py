from operator import add, mul

with open('inputs/day02.txt') as f:
    intcode = [int(num) for num in f.readline().split(',')]
    
intcode = intcode

class Computer:
    def __init__(self, intcode: list[int]):
        self.intcode = intcode
        self.op_codes = {1: add, 2: mul}
        self.finished_program = None
        
    def execute_intcode(self, noun=None, verb=None):
        intcode = [num for num in self.intcode]
        if noun:
            intcode[1] = noun
        if verb:
            intcode[2] = verb
            
        i = 0
        while True:
            code = intcode[i]
            if code == 99:
                break
            operation = self.op_codes[code]
            num1 = intcode[intcode[i+1]]
            num2 = intcode[intcode[i+2]]

            result = operation(num1, num2)
            intcode[intcode[i+3]] = result
            i += 4
        self.finished_program = intcode
        
    def get_result(self, noun=None, verb=None):
        self.execute_intcode(noun, verb)
        return self.finished_program[0]

computer = Computer(intcode)

# Part 1 solution.
print(computer.get_result(12, 2))

target = 19690720

for noun in range(100):
    for verb in range(100):
        if computer.get_result(noun, verb) == target:
            print(f'(100 * {noun}) + {verb} = {100*noun+verb}')
            break
