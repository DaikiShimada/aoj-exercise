# -*- coding: utf-8 -*-

import sys

def amida(w, side_bar):
    result = []
    side_bar.reverse()
    for x in range(1, w+1):
        status = x
        for bar in side_bar:
            if status == bar[0]:
                status = bar[1]
            elif status == bar[1]:
                status = bar[0]
        result.append(status)
    return result

def main():
    W = int(input())
    N = int(input())
    side_bar = [tuple(map(int, input().split(','))) for line in range(N)]
    result = amida(W, side_bar)
    for r in result:
        print(r)

if __name__ == '__main__':
    main()
