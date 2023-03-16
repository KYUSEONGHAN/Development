# https://www.acmicpc.net/problem/24313
# boj, 24313: 알고리즘 수업 - 점근적 표기 1, python3
def solve(a1: int, a0: int, c: int, n: int) -> int:
    return 1 if (a1 * n + a0 <= c * n) and (c >= a1) else 0


if __name__ == '__main__':
    a1, a0 = map(int, input().split())
    c = int(input())
    n = int(input())

    print(solve(a1, a0, c, n))