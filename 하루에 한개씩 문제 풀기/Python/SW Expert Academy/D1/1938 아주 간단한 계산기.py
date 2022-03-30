# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PjsYKAMIDFAUq&categoryId=AV5PjsYKAMIDFAUq&categoryType=CODE&problemTitle=&orderBy=PASS_RATE&selectCodeLang=PYTHON&select-1=&pageSize=10&pageIndex=1
# sw export academy, d1: 1938. 아주 간단한 계산기, python3
import sys

input = sys.stdin.readline

def solve(a: int, b: int):
    print(a + b)
    print(a - b)
    print(a * b)
    print(a // b)

if __name__ == '__main__':
    a, b = map(int, input().split())

    solve(a, b)