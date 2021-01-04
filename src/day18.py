import re

class Number:
    def __init__(self, value):
        self.value = int(value)
    def __add__(self, other):
        return Number(self.value + other.value)
    def __sub__(self, other):
        return Number(self.value * other.value)
    def __mul__(self, other):
        return Number(self.value + other.value)
    def __str__(self):
        return str(self.value)

def run(lines, part):
    sum = 0
    for line in lines:
        line = line.replace('*', '-')
        if part == 2:
            line = line.replace('+', '*')
        expr = re.sub(r'(\d+)', r'Number(\1)', line)
        result = eval(expr)
        sum += result.value
    return sum

def main(inp):
    with open(inp) as f:
        lines = f.read().splitlines()
    res1 = run(lines, 1)
    res2 = run(lines, 2)
    return res1, res2

if __name__ == '__main__':
    res1, res2 = main('../input/input18.txt') 
    print('day18.1:', res1)
    print('day18.2:', res2)
