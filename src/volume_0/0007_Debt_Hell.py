# -*- coding: utf-8 -*-

import sys

def debt_interest(debt, weeks, rate=0.05, cut_up=1000):
    if weeks != 1:
        debt = debt_interest(debt, weeks-1, rate=rate, cut_up=cut_up)

    debt *= 1 + rate
    c = debt % cut_up
    if c != 0:
        debt += cut_up - c
    return debt

def main():
    debt = 100000.
    n = int(input())
    ret = debt_interest(debt, n)
    print(int(ret))

if __name__ == '__main__':
    main()
