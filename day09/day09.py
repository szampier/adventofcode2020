import itertools

def part1(numbers):
    size = 25
    for i in range(len(numbers)):
        found = False
        for x, y in itertools.combinations(numbers[i:i+size], 2):
            if x + y == numbers[i+size]:
                found = True
        if not found:
            return numbers[i+size]

def part2(numbers, invalid_number):
    for i, n in enumerate(numbers):
        sum = n
        for j in range(i+1, len(numbers)):
            sum += numbers[j]
            seq = numbers[i:j+1]
            if sum == invalid_number:
                return min(seq) + max(seq)
            elif sum > invalid_number:
                break

def main(inp):
    lines = open(inp).read().splitlines()
    numbers = list(map(int, lines))
    invalid_number = part1(numbers)
    print('Part 1:', invalid_number)
    print('Part 2:', part2(numbers, invalid_number))

if __name__ == '__main__':
    main('input.txt')
