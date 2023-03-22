# https://www.acmicpc.net/problem/2444
# boj, 2444; 별 찍기 - 7, Python3
def solve(n: int):
    for x in range(1, n+1):
        print(' ' * (n-x) + '*' * (2*x-1))
    for x in range(n-1, 0, -1):
        print(' ' * (n-x) + '*' * (2*x-1))

if __name__ == '__main__':
    n = int(input())

    solve(n)