import itertools
from operator import itemgetter

def sieve(buses):
    """
    https://en.wikipedia.org/wiki/Chinese_remainder_theorem#Search_by_sieving
    """
    step, start = buses[0]
    for i, (bus, remainder) in enumerate(buses[1:]):
        for count in itertools.count(1):
            timestamp = start + count * step
            if timestamp % bus == remainder:
                step *= bus
                start = timestamp
                break
    return timestamp

def part1(lines):
    t0 = int(lines[0])
    buses = [int(x) for x in lines[1].split(',') if x != 'x']
    remainders = [((t0 // bus + 1) * bus) % t0 for bus in buses]
    index, min_value = min(enumerate(remainders), key=itemgetter(1))
    return min_value * buses[index]

def main(inp):
    with open(inp) as f:
        lines = f.read().splitlines()
    buses = [(int(bus), delay) for delay, bus in enumerate(lines[1].split(',')) if bus != 'x']
    buses = [(bus, (bus - delay) % bus) for bus, delay in buses]
    res1 = part1(lines)
    res2 = sieve(buses)
    return res1, res2

if __name__ == '__main__':
    res1, res2 = main('../input/input13.txt')
    print('day13.1:', res1)
    print('day13.2:', res2)
