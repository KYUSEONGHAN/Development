# https://www.acmicpc.net/problem/21300
# boj, 21300: bottle return, python3
import sys

input = sys.stdin.readline

def solve(datas: list) -> int:
    return sum([x * 5 for x in datas])

if __name__ == '__main__':
    datas = list(map(int, input().split()))

    print(solve(datas))