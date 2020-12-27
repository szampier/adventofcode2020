import re

required_fields = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])

def parse(lines):
    passports = []
    passport = {}
    for line in lines:
        if line == '':
            passports.append(passport)
            passport = {}
        else:
            for field in line.split():
                key, val = field.split(':')
                if key != 'cid':
                    passport[key] = val
    passports.append(passport)
    return passports

def has_required_fields(passport):
    return set(passport.keys()) == required_fields

def is_valid(p):
    byr=p['byr']; iyr=p['iyr']; eyr=p['eyr']
    hgt=p['hgt']; hcl=p['hcl']; ecl=p['ecl']
    pid=p['pid']
    return \
        len(byr) == 4 and 1920 <= int(byr) <= 2002 and \
        len(iyr) == 4 and 2010 <= int(iyr) <= 2020 and \
        len(eyr) == 4 and 2020 <= int(eyr) <= 2030 and \
        (hgt[-2:]=='cm' and 150 <= int(hgt[:-2]) <= 193 or \
        hgt[-2:]=='in' and 59 <= int(hgt[:-2]) <= 76) and \
        len(hcl) == 7 and hcl[0] == '#' and \
        ecl in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth') and \
        len(pid) == 9 and re.match(r'[0-9]', pid) is not None

def part1(passports):
    return len([p for p in passports if has_required_fields(p)])

def part2(passports):
    return len([p for p in passports if has_required_fields(p) and is_valid(p)])

def main(inp):
    lines = open(inp).read().splitlines()
    passports = parse(lines)
    print('Part 1:', part1(passports))
    print('Part 2:', part2(passports))

if __name__ == '__main__':
    main('input.txt')
