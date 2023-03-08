# https://www.acmicpc.net/problem/24265
# boj, 24265: 알고리즘 수업 - 알고리즘의 수행 시간 4, python3
def solve(n: int):
    print(n * (n - 1) // 2)
    print(2)

if __name__ == '__main__':
    n = int(input())

    solve(n)