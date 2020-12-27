def parse_line(line):
    return line.replace('-', ' ').replace(':', '').split()

def part1(lines):
    valid = 0
    for line in lines:
        min, max, letter, password = parse_line(line)
        if int(min) <= password.count(letter) <= int(max):
            valid += 1
    return valid

def part2(lines):
    valid = 0
    for line in lines:
        min, max, letter, password = parse_line(line)
        condition1 = password[int(min)-1] == letter
        condition2 = password[int(max)-1] == letter
        if (condition1 and not condition2) or (condition2 and not condition1):
            valid += 1
    return valid

def main(inp):
    lines = open(inp).read().splitlines()
    print('Part 1:', part1(lines))
    print('Part 2:', part2(lines))

if __name__ == '__main__':
    main('input.txt')
