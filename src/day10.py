def nC2(n):
    if n == 2:
        return 2
    if n == 3:
        return 4
    x = n - 1
    return 1 + x + x * (x-1) // 2

def part1(numbers):
    diffs = [m - n for m, n in zip(numbers[1:], numbers[:-1])]
    return diffs.count(1) * diffs.count(3)

def part2(numbers):
    seq_len = 0
    result = 1
    for m, n in zip(numbers[1:], numbers[:-1]):
        if m - n == 1:
            seq_len += 1
        else:
            result *= nC2(seq_len)
            seq_len = 0
    return result

def main(inp):
    with open(inp) as f:
        lines = f.read().splitlines()
    numbers = sorted([int(x) for x in lines])
    numbers = [0] + numbers + [numbers[-1] + 3]
    res1 = part1(numbers)
    res2 = part2(numbers)
    return res1, res2

if __name__ == '__main__':
    a, b = main('../input/input10.txt')
    print('day10.1:', a)
    print('day10.2:', b)
