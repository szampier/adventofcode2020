import copy

def parse(lines):
    instructions = []
    for line in lines:
        op, arg = line.split()
        instructions.append([op, int(arg)])
    return instructions

def change_at(program, index):
    op = program[index][0]
    new_op = None
    if op == 'nop':
        new_op = 'jmp'
    elif op == 'jmp':
        new_op = 'nop'
    else:
        return program
    new_program = copy.deepcopy(program)
    new_program[index][0] = new_op
    return new_program

def run(program):
    visited = []; sp = 0; acc = 0
    while sp not in visited and sp < len(program):
        visited.append(sp)
        op, arg = program[sp]
        if op == 'acc':
            acc += arg
            sp += 1
        elif op == 'nop':
            sp += 1
        elif op == 'jmp':
            sp += arg
    return acc, sp

def part2(program):
    for i, _ in enumerate(program):
        prog = change_at(program, i)
        acc, sp = run(prog)
        if sp == len(program):
            return acc

def main(inp):
    lines = open(inp).read().splitlines()
    program = parse(lines)
    print('Part 1:', run(program)[0])
    print('Part 2:', part2(program))

if __name__ == '__main__':
    main('input.txt')
