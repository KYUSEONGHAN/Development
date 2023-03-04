# https://www.acmicpc.net/problem/10813
# boj, 10813: 공 바꾸기, python3
def solve(n: int, m: int):
    ball = [x for x in range(1, n+1)]

    for x in range(m):
        a, b = map(int, input().split())
        ball[a-1], ball[b-1] = ball[b-1], ball[a-1]

    return ball

if __name__ == '__main__':
    n, m = map(int, input().split())

    print(*solve(n, m))