rows = list(range(128))
cols = list(range(8))

def find_row(rows, chars):
    l = len(rows)
    if l == 1:
        return rows[0]
    if chars[0] in ('F', 'L'):
        return find_row(rows[:l//2], chars[1:])
    else:
        return find_row(rows[l//2:], chars[1:])

def part2(seats):
    seats.sort()
    for i, n in enumerate(seats[1:-1]):
        if seats[i] != n-1:
            return (n-1)
        if seats[i+2] != n+1:
            return (n+1)

def main(inp):
    with open(inp) as f:
        lines = f.read().splitlines()
    seats = [8 * find_row(rows, line[:7]) + find_row(cols, line[-3:]) for line in lines]
    res1 = max(seats)
    res2 = part2(seats)
    return res1, res2

if __name__ == '__main__':
    a, b = main('../input/input05.txt')
    print('day05.1:', a)
    print('day05.2:', b)
