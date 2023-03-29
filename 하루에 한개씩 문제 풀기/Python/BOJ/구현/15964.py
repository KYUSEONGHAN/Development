# https://www.acmicpc.net/problem/15964
# boj, 15964: 이상한 기호, Python3
def solve(a: int, b: int) -> int:
    return (a + b) * (a - b)

if __name__ == '__main__':
    a, b = map(int, input().split())

    print(solve(a, b))