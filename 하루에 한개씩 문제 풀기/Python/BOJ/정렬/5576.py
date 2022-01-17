# boj, 5576: 콘테스트, python3
import sys

input = sys.stdin.readline

def solve():
    w = sorted([int(input()) for _ in range(10)], reverse=True)[:3]
    k = sorted([int(input()) for _ in range(10)], reverse=True)[:3]

    return sum(w), sum(k)

if __name__ == '__main__':
    print(*solve())