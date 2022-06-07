# https://www.acmicpc.net/problem/1931
# boj, 1931: 회의실 배정, python3
import sys

input = sys.stdin.readline  # 변수 입력 속도 향상

# 사용할 수 있는 회의의 최대 개수를 구하는 함수
def solve(meeting_info: list) -> int:
    meeting_info = sorted(meeting_info, key=lambda x: (x[1], x[0]))  # 회의가 끝나는 시간 -> 회의가 시작하는 시간순으로 정렬
    result = 0  # 회의 최대 개수를 담는 변수
    start = 0

    for meeting in meeting_info:  # 주어진 회의 시간으로 반복문 순회
        if meeting[0] >= start:   # 현재 요소의 회의 시작 시간이 start 변수보다 같거나 크다면
            start = meeting[1]    # start를 현재 요소의 종료 시간으로 swap
            result += 1

    return result  # 결과값 반환

if __name__ == '__main__':
    n = int(input())  # 회의의 수
    meeting_info = [list(map(int, input().split())) for _ in range(n)]  # 회의의 정보

    print(solve(meeting_info))