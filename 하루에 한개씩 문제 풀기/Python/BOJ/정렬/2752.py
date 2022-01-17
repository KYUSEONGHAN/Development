# boj, 2752: 세수정렬, python3
import sys

input = sys.stdin.readline

def solve(num):
    return sorted(num)

if __name__ == '__main__':
    num = list(map(int, input().split()))

    print(*solve(num))