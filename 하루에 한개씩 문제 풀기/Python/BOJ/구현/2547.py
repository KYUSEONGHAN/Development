# https://www.acmicpc.net/problem/2547
# boj, 2547: 사탕 선생 고창영, python3
def solve(student: list) -> str:
    return 'YES' if sum(student) % len(student) == 0 else 'NO'

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        _ = input()
        n = int(input())
        student = [int(input()) for _ in range(n)]

        print(solve(student))