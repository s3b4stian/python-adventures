

import images
import random
import sys

import program01 as program
from itertools import starmap

spaces = ' '*20 + '\t'*5

def genera_matrice( maxrows, maxcols, maxsize, spaziatura ):
    rows = random.randint(maxrows//2, maxrows)
    filename = f'mat-{rows}-{spaziatura}.txt'
    matrix = []
    WIDTHS = []
    for _ in range(rows):
        cols = 1+2*random.randint(1, maxcols) if random.randint(1,100)>20 else 1
        row  = []
        w    = spaziatura
        for _ in range(cols):
            W = 2*random.randint(3, maxsize)
            H = 2*random.randint(3, maxsize)
            row.append([W,H])
            w += W + spaziatura
        matrix.append(row)
        WIDTHS.append(w)
    MAX = max(WIDTHS)
    for row,w in zip(matrix, WIDTHS):
        N   = len(row)
        if N > 1:
            diff = MAX-w
            rest = diff % (N-1)
            if rest:
                print(f"fixing line\t{w=}\t{MAX=}\t{diff=}\t{N=}\t{rest=}")
                row[0][0] += rest
            assert (MAX-(sum( [ wi+spaziatura for wi,he in row ] )+spaziatura)) % (N-1) == 0
    with open(filename, mode='w', encoding='utf-8') as F:
        for row in matrix:
            for W,H in row:
                R = random.randint(100, 255)
                G = random.randint(100, 255)
                B = random.randint(100, 255)
                for v in [W,H,R,G,B]:
                    n = random.randint(0,10)
                    m = random.randint(0,10)
                    o = random.randint(0,10)
                    pre  = ''.join(random.choices(spaces, k=m))
                    intr = ''.join(random.choices(spaces, k=n))
                    post = ''.join(random.choices(spaces, k=o))
                    print(f'{pre}{v}{intr},{post}',end='', file=F)
            print(file=F)

if __name__ == '__main__':
    if len(sys.argv) == 5:
        genera_matrice(*map(int, sys.argv[1:5]))
    else:
        print('Usage: genera maxrows maxcols maxsize spaziatura')

