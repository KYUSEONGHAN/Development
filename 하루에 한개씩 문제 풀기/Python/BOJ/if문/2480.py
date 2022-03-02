# https://www.acmicpc.net/problem/2480
# boj, 2480: 주사위새개, python3
import sys

input = sys.stdin.readline

def solve(a, b, c):
    if a == b == c:
        return 10000 + a*1000
    elif a != b and a != c and b != c:
        return max(a, b, c) * 100
    else:
        d = [0] * 7
        d[a] += 1
        d[b] += 1
        d[c] += 1

    return 1000 + (d.index(max(d)) * 100)

if __name__ == '__main__':
    a, b, c = map(int, input().split())

    print(solve(a, b, c))