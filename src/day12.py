import sys

def wrap(angle):
    return (360 + angle) % 360

def left(wp, val):
    x0, y0 = wp
    if val == 90:
        x1 = -y0
        y1 = x0
    elif val == 180:
        x1 = -x0
        y1 = -y0
    elif val == 270:
        x1 = y0
        y1 = -x0
    else:
        assert False
    return [x1, y1]

def right(wp, val):
    x0, y0 = wp
    if val == 90:
        x1 = y0
        y1 = -x0
    elif val == 180:
        x1 = -x0
        y1 = -y0
    elif val == 270:
        x1 = -y0
        y1 = x0
    else:
        assert False
    return [x1, y1]

def part1(commands):
    angle2cmd = {0: 'E', 90: 'N', 180: 'W', 270: 'S'}
    angle, x, y = 0, 0, 0
    for cmd, val in commands:
        cmd = angle2cmd[angle] if cmd == 'F' else cmd
        if cmd == 'L':
            angle = wrap(angle + val)
        elif cmd == 'R':
            angle = wrap(angle - val)
        elif cmd == 'N':
            y += val
        elif cmd == 'S':
            y -= val
        elif cmd == 'E':
            x += val
        elif cmd == 'W':
            x -= val
        else:
            assert False
    return abs(x) + abs(y)

def part2(commands):
    ship = [0, 0]
    waypoint = [10, 1]
    for cmd, val in commands:
        if cmd == 'L':
            waypoint = left(waypoint, val)
        elif cmd == 'R':
            waypoint = right(waypoint, val)
        elif cmd == 'F':
            ship[0] += waypoint[0] * val
            ship[1] += waypoint[1] * val
        elif cmd == 'N':
            waypoint[1] += val
        elif cmd == 'S':
            waypoint[1] -= val
        elif cmd == 'E':
            waypoint[0] += val
        elif cmd == 'W':
            waypoint[0] -= val
        else:
            assert False
    return abs(ship[0]) + abs(ship[1])

def main(inp):
    with open(inp) as f:
        lines = f.read().splitlines()
    commands = [(x[0], int(x[1:])) for x in lines]
    res1 = part1(commands)
    res2 = part2(commands)
    return res1, res2

if __name__ == '__main__':
    res1, res2 = main('../input/input12.txt')
    print('day12.1:', res1)
    print('day12.2:', res2)
