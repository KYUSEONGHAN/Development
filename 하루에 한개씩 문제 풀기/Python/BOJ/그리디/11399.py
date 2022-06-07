# https://www.acmicpc.net/problem/11399
# boj, 11399: atm, python3
import sys

input = sys.stdin.readline  # 변수 입력 속도 향상

# 각 사람이 돈을 인출하느데 필요한 시간의 합의 최솟값을 구하는 함수
def solve(times: list) -> int:
    result = []   # 결과값을 담을 list
    money_time = 0  # 가중치 담을 변수

    times = sorted(times)  # 주어진 시간 list를 오름차순 정렬

    for time in times:     # times list for 반복문으로 순회
        money_time += time  # 현재 요소를 가중치 변수에 추가
        result.append(money_time)  # 가중치를 결과 list에 추가

    return sum(result) # 결과 반환

if __name__ == '__main__':
    n = int(input())  # n: 사람의 수
    pi = list(map(int, input().split()))  # pi: 각 사람이 돈을 인출하는데 걸리는 시간

    print(solve(pi))