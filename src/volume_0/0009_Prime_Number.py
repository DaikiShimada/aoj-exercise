# -*- coding: utf-8 -*-

import sys


def eratosthenes_sieve(n):
    table = [0]*(n + 1)
    prime_list = []
    
    for i in range(2, n + 1):
        if table[i] == 0:
            prime_list.append(i)
            for j in range(i + i, n + 1, i):
                table[j] = 1
    return prime_list


def prime(n):
    return eratosthenes_sieve(n)

def main():
    inp = [int(n) for n in sys.stdin]
    for n in inp:
        n_pn = len(prime(n))
        print(n_pn)

if __name__ == '__main__':
    main()
