from collections import defaultdict
from functools import reduce

def parse_ranges(lines):
    ranges = []
    for line in lines:
        if line == '':
            return ranges
        _, stuff = line.split(':')
        items = stuff.replace('or','').replace('-',' ').split()
        items = [int(i) for i in items]
        ranges.append([items[0],items[1],items[2],items[3]])

def parse_ticket(lines):
    ix = lines.index('your ticket:')
    return [int(t) for t in lines[ix+1].split(',')]

def parse_tickets(lines):
    tickets = []
    ix = lines.index('nearby tickets:')
    for i in range(ix+1, len(lines)):
        ticket = [int(t) for t in lines[i].split(',')]
        tickets.append(ticket)
    return tickets

def part1(tickets, ranges):
    errors = 0
    valid_tickets = []
    for ticket in tickets:
        valid = True
        for value in ticket:
            if all([value<a or b<value<c or value>d for a,b,c,d in ranges]):
                errors += value
                valid = False
        if valid:
            valid_tickets.append(ticket)
    return errors, valid_tickets

def clean(map, element):
    for value in map.values():
        if len(value) > 1 and element in value:
            value.remove(element)

def part2(tickets, ticket, ranges):
    cols = set()
    map = defaultdict(list)
    for col in range(len(ticket)):
        column = [t[col] for t in tickets]
        for range_id,(a,b,c,d) in enumerate(ranges):
            if all([a<=x<=b or c<=x<=d for x in column]):
                cols.add(col)
                map[range_id].append(col)
    
    for _ in range(len(ticket)):
        for value in map.values():
            if len(value) == 1:
                clean(map, value[0])
    
    values = [ticket[v[0]] for k,v in map.items() if k<6]
    res = reduce((lambda x, y: x * y), values)
    return res

def main(inp):
    with open(inp) as f:
        lines = f.read().splitlines()
    ranges = parse_ranges(lines)
    ticket = parse_ticket(lines)
    tickets = parse_tickets(lines)
    res1, tickets = part1(tickets, ranges)
    res2 = part2(tickets, ticket, ranges)
    return res1, res2

if __name__ == '__main__':
    res1, res2 = main('../input/input16.txt')
    print('day16.1:', res1)
    print('day16.2:', res2)
