def run(numbers, nth):
    last = numbers[-1]
    numbers = {n:i+1 for i, n in enumerate(numbers[:-1])}
    for i in range(len(numbers)+1, nth):
        if last in numbers:
            value = i - numbers[last]
        else:
            value = 0
        numbers[last] = i
        last = value
    return last

def main(inp):
    with open(inp) as f:
        lines = f.read().splitlines()
    numbers = [int(n) for n in lines[0].split(',')]
    res1 = run(numbers, 2020)
    res2 = run(numbers, 30000000)
    return res1, res2

if __name__ == '__main__':
    res1, res2 = main('../input/input15.txt')
    print('day15.1:', res1)
    print('day15.2:', res2)
