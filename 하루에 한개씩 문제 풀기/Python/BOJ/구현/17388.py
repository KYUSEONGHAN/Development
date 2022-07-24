# https://www.acmicpc.net/problem/17388
# boj, 17388: 와글와글 숭고한, python3
import sys

input = sys.stdin.readline

# 연합 대학교 동아리 참여율 확인하는 함수
def solve(s: int, k: int, h: int) -> str:
    if s + k + h >= 100:
        return 'OK'

    if s < k and s < h:
        return 'Soongsil'
    elif k < s and k < h:
        return 'Korea'
    elif h < s and h < k:
        return 'Hanyang'

if __name__ == '__main__':
    s, k, h = map(int, input().split())

    print(solve(s, k, h))