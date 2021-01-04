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
    with open(inp) as f:
        lines = f.read().splitlines()
    res1 = part1(lines)
    res2 = part2(lines)
    return res1, res2

if __name__ == '__main__':
    a, b = main('../input/input02.txt')
    print('day02.1:', a)
    print('day02.2:', b)
