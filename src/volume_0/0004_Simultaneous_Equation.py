# -*- coding: utf-8 -*-

import sys

def solve_sim_equ(a, b, c, d, e, f):
    '''
    This function solves following equation.
    ax + by = c
    dx + ey = f
    '''
    if a==0 and d==0:
        if b==0 and e==0:
            return 0., 0.
        if b != 0:
            return 0., c/b+0.
        else:
            return 0., f/e+0.
    elif b==0 and e==0:
        if a != 0:
            return 0., d/a+0.
        else:
            return 0., a/d+0.

    if b == 0:
        a, d = d, a
        b, e = e, b
        c, f = f, c
    g = e / b
    x = (g*c - f) / (g*a - d)
    y = (c - a*x) / b
    return x+0., y+0.

def main():
    for line in sys.stdin:
        a,b,c,d,e,f = map(float, line.split())
        x, y = solve_sim_equ(a, b, c, d, e, f)
        print('{0:.3f} {1:.3f}'.format(x,y))

if __name__ == '__main__':
    main()
