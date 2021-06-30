# boj, 2309 : 일곱 난쟁이, python3
# 브루트포스 알고리즘
import sys
from itertools import combinations

def dwarf(l):
    for i in list(combinations(l, 7)):
        if sum(i) == 100:
            return '\n'.join(map(str, sorted(i)))

h = [int(sys.stdin.readline()) for i in range(9)]

print(dwarf(h))