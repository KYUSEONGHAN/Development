# https://www.acmicpc.net/problem/25305
# boj, 25305: 커트라인, python3
import sys

input = sys.stdin.readline

# 상을 받는 커트라인이 몇 점인지 구하는 함수
def solve(x: list, num: int) -> int:
    return sorted(x, reverse=True)[num-1]  # 점수 높은대로 내림차순 정렬한 뒤, 상을 받는 사람 수 -1 번째 반환

if __name__ == '__main__':
    n, k = map(int, input().split())     # n: 응시자 수, k: 상을 받는 사람의 수
    x = list(map(int, input().split()))  # x: 각 학생의 점수

    print(solve(x, k))