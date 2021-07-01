# boj, 1271 : 엄청난 부자2, python3
import sys

def super_rich(n, m):
    result = [n//m, n%m]
    return '\n'.join(map(str, result))

n, m = map(int, sys.stdin.readline().split())

print(super_rich(n, m))