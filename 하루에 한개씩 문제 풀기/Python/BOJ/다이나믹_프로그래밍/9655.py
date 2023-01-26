# https://www.acmicpc.net/problem/9655
# boj, 9655: 돌 게임, python3
import sys

input = sys.stdin.readline

def solve(n: int) -> str:
    return 'SK' if n % 2 != 0 else 'CY'

if __name__ == '__main__':
    # 첫째 줄에 N이 주어진다. (1 ≤ N ≤ 1000)
    n = int(input())

    # 상근이가 게임을 이기면 SK를, 창영이가 게임을 이기면 CY을 출력한다.
    print(solve(n))