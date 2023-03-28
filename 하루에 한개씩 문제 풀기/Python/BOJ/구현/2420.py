# https://www.acmicpc.net/problem/2420
# boj, 2420: 사파리월드, python3
def solve(n: int, m: int) -> int:
    return abs(n-m)

if __name__ == '__main__':
    n, m = map(int, input().split())

    print(solve(n, m))