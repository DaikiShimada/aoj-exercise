# -*- coding: utf-8 -*-

import sys

def sum_intergers(n, k=4, last=True):
    clip_9 = lambda x: x if x < 10 else 9

    if k > 1:
        c = sum_intergers(n, k=k-1, last=False)
    else:
        return [(s,) for s in range(clip_9(n)+1)]

    ret = []
    for cc in c:
        sum_cc = sum(cc) # memorize
        for s in range(clip_9(n-sum_cc)+1):
            if not last or s+sum_cc==n:
                r = [p for p in cc]
                r.append(s)
                ret.append(tuple(r))
    return ret


def main():
    ns = [int(n) for n in sys.stdin]
    for n in ns:
        c = len(sum_intergers(n, k=4))
        print(c)


if __name__ == '__main__':
    main()
