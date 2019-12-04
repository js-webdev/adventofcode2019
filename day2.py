"""
Day 2
"""

def solutionStar1(inputFile, noun, verb):
    with open(inputFile, "r") as input:
        memory = [int(numericString) for numericString in input.read().split(",")]
        memory[1] = noun
        memory[2] = verb
        opcode = 0
        instructionPointer = 0

        while True:
            opcode = memory[instructionPointer]
            
            if (opcode == 99):
                break

            parameter1 = memory[instructionPointer + 1]
            parameter2 = memory[instructionPointer + 2]
            parameter3 = memory[instructionPointer + 3]

            if (opcode == 1):
               memory[parameter3] = memory[parameter1] + memory[parameter2]

            if (opcode == 2):
               memory[parameter3] = memory[parameter1] * memory[parameter2]

            instructionPointer += 4

        return memory[0]

def part1():
    return solutionStar1('day2-input.txt', 12,2)


def part2():
    for noun in range(0,99):
        for verb in range(0, 99):
            result = solutionStar1('day2-input.txt', noun, verb)
            if (result == 19690720):
                return noun * 100 + verb 

# part1(lines)

print(part1())
print(part2())