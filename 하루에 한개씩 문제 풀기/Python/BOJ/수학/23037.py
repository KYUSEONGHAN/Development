# https://www.acmicpc.net/problem/23037
# boj, 23037: 5의 수난, python3
from math import pow

def solve(n: str) -> int:
    return int(sum([pow(int(x), 5) for x in n]))

if __name__ == '__main__':
    n = input()

    print(solve(n))