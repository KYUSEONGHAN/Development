# boj, 11729 : 하노이 탑 이동 순서, python3
import sys

def hanoi(n, s, e, b):
    if n == 1:
        print(s, end=' ')
        print(e)
        return
    hanoi(n - 1, s, b, e)
    print(s, end=' ')
    print(e)
    hanoi(n - 1, b, e, s)


N = int(sys.stdin.readline())
k = 2 ** N - 1
print(k)
hanoi(N, 1, 3, 2)