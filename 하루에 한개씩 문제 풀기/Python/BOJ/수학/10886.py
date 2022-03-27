# https://www.acmicpc.net/problem/10886
# boj, 10886: 0 = not cute / 1 = cute, python3
import sys

input = sys.stdin.readline

def solve(n: int) -> str:
    own, zero = 0, 0

    for _ in range(n):
        number = int(input())

        if number == 1:
            own += 1
        else:
            zero += 1

    return 'Junhee is cute!' if own > zero else 'Junhee is not cute!'

if __name__ == '__main__':
    n = int(input())

    print(solve(n))