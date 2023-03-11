# https://www.acmicpc.net/problem/24267
# boj, 24267: 알고리즘 수업 - 알고리즘의 수행 시간 6, python3
def solve(n: int):
    print(n * (n-1) * (n-2) // 6)
    print(3)

if __name__ == '__main__':
    n = int(input())

    solve(n)