#!/usr/bin/python

import math
import requests
from collections import Counter

shakespeare = requests.get('https://ocw.mit.edu/ans7870/6/6.006/s08/'
                           'lecturenotes/files/t8.shakespeare.txt').text
eng_freq = Counter(shakespeare)


def score_string(string: str) -> float:
    a = eng_freq
    b = Counter(string)
    shared_keys = set(a.keys()).intersection(set(b.keys()))
    top = sum([a[k] * b[k] for k in shared_keys])
    bottom = (math.sqrt(sum([v * v for v in a.values()])) *
              math.sqrt(sum([v * v for v in b.values()])))

    v = top / bottom
    return v


def main(*args):
    return score_string(' '.join([str(x) for x in args]))


if __name__ == '__main__':
    import sys
    print(main(*sys.argv))
