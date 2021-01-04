def count_trees(lines, right, down):
    count = 0
    index = 0
    for i, line in enumerate(lines):
        if i % down != 0:
            continue
        if line[index % 31] == '#':
            count += 1
        index += right
    return count

def main(inp):
    with open(inp) as f:
        lines = f.read().splitlines()
    part1 = count_trees(lines, 3, 1)
    part2 = part1
    part2 *= count_trees(lines, 1, 1)
    part2 *= count_trees(lines, 5, 1)
    part2 *= count_trees(lines, 7, 1)
    part2 *= count_trees(lines, 1, 2)
    return part1, part2

if __name__ == '__main__':
    a, b = main('../input/input03.txt')
    print('day03.1:', a)
    print('day03.2:', b)
