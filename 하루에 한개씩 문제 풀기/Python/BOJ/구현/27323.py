# https://www.acmicpc.net/problem/27323
# boj, 27323: 직사각형, Python3
def solve(a: int, b: int) -> int:
    return a * b

if __name__ == '__main__':
    a = int(input())
    b = int(input())

    print(solve(a, b))