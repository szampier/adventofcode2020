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
    lines = open(inp).read().splitlines()
    numbers = list(map(int, lines))
    print('day01.1:', part1(numbers))
    print('day01.2:', part2(numbers))

if __name__ == '__main__':
    main('../input/input01.txt')
