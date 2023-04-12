# https://www.acmicpc.net/problem/3460
# boj, 3460: 이진수, Python3
def solve(t: int):
    for _ in range(t):
        num = format(int(input()), 'b')

        for index, x in enumerate(list(reversed(str(num)))):
            if x == '1':
                print(index, end=' ')

if __name__ == '__main__':
    t = int(input())

    solve(t)