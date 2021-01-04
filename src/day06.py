def parse(lines):
    group = []
    groups = []
    for line in lines:
        if line == '':
            groups.append(group)
            group = []
        else:
            group.append(set(line))
    groups.append(group)
    return groups

def part1(groups):
    count = 0
    for group in groups:
        count += len(set.union(*group))
    return count

def part2(groups):
    count = 0
    for group in groups:
        count += len(set.intersection(*group))
    return count

def main(inp):
    with open(inp) as f:
        lines = f.read().splitlines()
    groups = parse(lines)
    res1 = part1(groups)
    res2 = part2(groups)
    return res1, res2

if __name__ == '__main__':
    a, b = main('../input/input06.txt')
    print('day06.1:', a)
    print('day06.2:', b)
