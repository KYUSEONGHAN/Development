# https://www.acmicpc.net/problem/25238
# boj, 25238: 가희와 방어율 무시, python3
import sys

input = sys.stdin.readline

# 몬스터에게 대미지를 줄 수 있는지 확인하는 함수
def solve(a: int, b: int) -> int:
    return 0 if a * ((100-b) / 100) >= 100 else 1

if __name__ == '__main__':
    a, b = map(int, input().split())

    print(solve(a, b))