from collections import Counter
from copy import deepcopy
from itertools import chain

def adjacent(m, i, j):
    nrows = len(m)
    ncols = len(m[0])
    adj = [(i-1, j-1), (i-1, j), (i-1, j+1),
           (i+1, j-1), (i+1, j), (i+1, j+1),
           (i, j-1), (i, j+1)]
    return [m[x][y] for x, y in adj if 0 <= x < nrows and 0 <= y < ncols]

def up_right(m, i, j):
    nrows = len(m)
    ncols = len(m[0])
    for t in range(1,nrows):
        ii = i-t;
        if ii < 0: return None
        jj = j+t;
        if jj > ncols-1: return None
        x = m[ii][jj];
        if x in ('L','#'): return x
    return None

def up_left(m, i, j):
    nrows = len(m)
    ncols = len(m[0])
    for t in range(1,nrows):
        ii = i-t;
        if ii < 0: return None
        jj = j-t;
        if jj < 0: return None
        x = m[ii][jj];
        if x in ('L','#'): return x
    return None

def down_right(m, i, j):
    nrows = len(m)
    ncols = len(m[0])
    for t in range(1,nrows):
        ii = i+t;
        if ii > nrows-1: return None
        jj = j+t;
        if jj > ncols-1: return None
        x = m[ii][jj];
        if x in ('L','#'): return x
    return None

def down_left(m, i, j):
    nrows = len(m)
    ncols = len(m[0])
    for t in range(1,nrows):
        ii = i+t;
        if ii > nrows-1: return None
        jj = j-t;
        if jj < 0: return None
        x = m[ii][jj];
        if x in ('L','#'): return x
    return None

def right(m, i, j):
    nrows = len(m)
    ncols = len(m[0])
    for t in range(1,nrows):
        jj = j+t;
        if jj > ncols-1: return None
        x = m[i][jj];
        if x in ('L','#'): return x
    return None


def left(m, i, j):
    nrows = len(m)
    ncols = len(m[0])
    for t in range(1,nrows):
        jj = j-t;
        if jj < 0: return None
        x = m[i][jj];
        if x in ('L','#'): return x
    return None

def down(m, i, j):
    nrows = len(m)
    ncols = len(m[0])
    for t in range(1,nrows):
        ii = i+t;
        if ii > nrows-1: return None
        x = m[ii][j];
        if x in ('L','#'): return x
    return None

def up(m, i, j):
    nrows = len(m)
    ncols = len(m[0])
    for t in range(1,nrows):
        ii = i-t;
        if ii < 0: return None
        x = m[ii][j];
        if x in ('L','#'): return x
    return None

def get_vis(m, i, j):
    res = []
    res.append(up(m,i,j))
    res.append(down(m,i,j))
    res.append(right(m,i,j))
    res.append(left(m,i,j))
    res.append(up_right(m,i,j))
    res.append(up_left(m,i,j))
    res.append(down_right(m,i,j))
    res.append(down_left(m,i,j))
    return [x for x in res if x is not None]

def change1(mat):
    nrows = len(mat)
    ncols = len(mat[0])
    new_mat = deepcopy(mat)
    for i in range(nrows):
        for j in range(ncols):
            adj = adjacent(mat, i, j)
            c = Counter(adj)
            if mat[i][j] == 'L' and c['#'] == 0:
                new_mat[i][j] = '#'
            elif mat[i][j] == '#' and c['#'] >= 4:
                new_mat[i][j] = 'L'
    return new_mat

def change2(mat):
    nrows = len(mat)
    ncols = len(mat[0])
    new_mat = deepcopy(mat)
    for i in range(nrows):
        for j in range(ncols):
            adj = get_vis(mat, i, j)
            c = Counter(adj)
            if mat[i][j] == 'L' and c['#'] == 0:
                new_mat[i][j] = '#'
            elif mat[i][j] == '#' and c['#'] >= 5:
                new_mat[i][j] = 'L'
    return new_mat

def run(m1, change):
    while True:
        m2 = change(m1)
        if m1 == m2:
            break
        else:
            m1 = m2
    c = Counter(chain.from_iterable(m2))
    return c['#']

def main(inp):
    with open(inp) as f:
        lines = f.read().splitlines()
    mat = [[c for c in line] for line in lines]
    res1 = run(mat, change1)
    res2 = run(mat, change2)
    return res1, res2

if __name__ == '__main__':
    res1, res2 = main('../input/input11.txt')
    print('day11.1:', res1)
    print('day11.2:', res2)
