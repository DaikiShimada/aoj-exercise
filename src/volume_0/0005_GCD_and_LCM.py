# -*- coding: utf-8 -*-

import sys

def gcd(a, b):
    if a < b:
        a, b = b, a
    while b!=0:
        c = b
        b = a % b
        a = c
    return a

def lcm(a, b, g):
    return a * b / g

def main():
    for line in sys.stdin:
        a, b = map(int, line.split())
        ng = gcd(a, b)
        nl = lcm(a, b, ng)
        print('{0:d} {1:d}'.format(int(ng), int(nl)))

if __name__ == '__main__':
    main()
