# -*- coding: utf-8 -*-

import sys
import six

def top_k_sort(data, k=3, reverse=True):
    data.sort(reverse=True)
    return data[:k]

def main():
    data = map(int, raw_input().split())

    data = [int(v) for v in argv[1:]]
    for h in top_k_sort(data):
        print(h)

if __name__ == '__main__':
    main()
