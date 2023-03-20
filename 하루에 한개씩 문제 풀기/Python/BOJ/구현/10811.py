# https://www.acmicpc.net/problem/10811
# boj, 10811: 바구니 뒤집기, python3
def solve(n:int, l: list) -> list:
    data = [x for x in range(1, n+1)]

    for x in l:
        data[x[0]-1:x[1]] = data[x[0]-1:x[1]][::-1]

    return data

if __name__ == '__main__':
    n, m = map(int, input().split())
    l = [list(map(int, input().split())) for _ in range(m)]

    print(*solve(n, l))