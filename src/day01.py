import itertools

def part1(numbers):
    for x, y in itertools.combinations(numbers, 2):
        if x + y == 2020:
            return x * y

def part2(numbers):
    for x, y, z in itertools.combinations(numbers, 3):
        if x + y + z == 2020:
            return x * y * z

def main(inp):
    with open(inp) as f:
        lines = f.read().splitlines()
    numbers = list(map(int, lines))
    res1 = part1(numbers)
    res2 = part2(numbers)
    return res1, res2

if __name__ == '__main__':
    a, b = main('../input/input01.txt')
    print('day01.1:', a)
    print('day01.2:', b)
