from collections import defaultdict

def parse_input(inp):
    bags = defaultdict(list)
    lines = open(inp).read().splitlines()
    for line in lines:
        items = line.replace(',','').replace('.','').split()
        if items[-2] == 'other':
            continue
        key = items[0] + items[1]
        for i in range(4, len(items), 4):
            qty = int(items[i])
            color = items[i+1] + items[i+2]
            bags[key].append((qty, color))
    return bags

def contains_shinygold(bags, bag):
    for qty, color in bags[bag]:
        if color == 'shinygold':
            return True
        elif color in bags:
            if contains_shinygold(bags, color):
                return True
    return False

def part1(bags):
    count = 0
    for bag in bags:
        if contains_shinygold(bags, bag):
            count += 1
    return count

def part2(bags, bag):
    count = 1
    for qty, color in bags.get(bag, []):
        count += qty * part2(bags, color)
    return count

def main(inp):
    bags = parse_input(inp)
    print('Part 1:', part1(bags))
    print('Part 2:', part2(bags, 'shinygold') - 1)

if __name__ == '__main__':
    main('input.txt')
