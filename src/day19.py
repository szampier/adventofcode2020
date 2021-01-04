from itertools import chain
import re

def get_line8():
    ret = ['8']
    for i in range(1, 10):
        for j in range(1, i+1):
            ret.append('42')
        ret.append('|')
    return ret[:-1]

def get_line11():
    ret = ['11']
    for i in range(1, 10):
        for j in range(1, i+1):
            ret.append('42')
        for j in range(1, i+1):
            ret.append('31')
        ret.append('|')
    return ret[:-1]

def parse_rules(lines, part):
    rules = {}
    for line in lines:
        if line == '':
            break
        else:
            items = line.replace(':', '').replace('"', '').split()
            if part == 2 and items[0] == '8':
                items = get_line8()
            elif part == 2 and items[0] == '11':
                items = get_line11()
            rules[items[0]] = items[1:]
    return rules

def build_regex(rules, key):
    if key in ('a', 'b', '|'):
        return key
    else:
        return '({})'.format(''.join([build_regex(rules, v) for v in rules.get(key, [])]))

def get_regex(lines, part):
    rules = parse_rules(lines, part)
    regex = build_regex(rules, '0')
    return regex.replace('(a)', 'a').replace('(b)', 'b').replace('()', '')
    
def run(messages, regex):
    pattern = re.compile(regex + '$')
    matches = [1 for msg in messages if pattern.match(msg) is not None]
    return len(matches)

def main(inp):
    with open(inp) as f:
        lines = f.read().splitlines()
    messages = [line for line in lines if len(line) > 0 and line[0] in ('a', 'b')]
    regex = get_regex(lines, 1)
    res1 = run(messages, regex)
    regex = get_regex(lines, 2)
    res2 = run(messages, regex)
    return res1, res2

if __name__ == '__main__':
    res1, res2 = main('../input/input19.txt')
    print('day19.1:', res1)
    print('day19.2:', res2)
