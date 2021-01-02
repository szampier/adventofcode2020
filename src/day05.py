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
    lines = open(inp).read().splitlines()
    seats = [8 * find_row(rows, line[:7]) + find_row(cols, line[-3:]) for line in lines]
    print('day05.1:', max(seats))
    print('day05.2:', part2(seats))

if __name__ == '__main__':
    main('../input/input05.txt')
