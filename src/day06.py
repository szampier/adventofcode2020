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
    lines = open(inp).read().splitlines()
    groups = parse(lines)
    print('day06.1:', part1(groups))
    print('day06.2:', part2(groups))

if __name__ == '__main__':
    main('../input/input06.txt')
