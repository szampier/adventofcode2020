import itertools

def apply_mask_to_value(value, mask):
    addr_bits = [b for b in f'{value:036b}']
    for i, bit in enumerate(mask):
        if bit != 'X': addr_bits[i] = bit
    return int(''.join(addr_bits), 2)

def apply_mask_to_addr(addr, mask):
    addr_bits = [b for b in f'{addr:036b}']
    indexes = []
    for i, bit in enumerate(mask):
        if bit == '1': addr_bits[i] = bit
        if bit == 'X': indexes.append(i)
    addrs = []
    for pattern in itertools.product(['0','1'], repeat=len(indexes)):
        for i, bit in enumerate(pattern):
            addr_bits[indexes[i]] = bit
        addrs.append(''.join(addr_bits))
    return addrs

def run(lines, part):
    mem = {}
    mask = None
    for line in lines:
        items = line.replace('[',' ').replace(']', ' ').split()
        if items[0] == 'mask':
            mask = items[2]
        else:
            addr = int(items[1])
            value = int(items[3])
            if part == 1:
                mem[addr] = apply_mask_to_value(value, mask)
            else:
                for addr in apply_mask_to_addr(addr, mask):
                    mem[addr] = value
    return sum(mem.values())

def main(inp):
    with open(inp) as f:
        lines = f.read().splitlines()
    res1 = run(lines, 1)
    res2 = run(lines, 2)
    return res1, res2

if __name__ == '__main__':
    res1, res2 = main('../input/input14.txt')
    print('day14.1:', res1)
    print('day14.2:', res2)
