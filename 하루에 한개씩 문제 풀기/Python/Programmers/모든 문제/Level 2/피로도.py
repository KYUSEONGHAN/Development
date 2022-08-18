# https://school.programmers.co.kr/learn/courses/30/lessons/87946
# programmers, level2: 피로도, python3
from itertools import permutations

def solution(k: int, dungeons: list) -> int:
    permu, result = list(permutations(range(len(dungeons)))), 0  # permu: list의 길이만큼 경우의 수 할당

    for x in permu:  # 구한 순열을 for 반복문으로 순회
        piro, pre_result = k, 0  # 현재 반복문에서 유저가 탐험할 수 있는 던전 수
        for y in x:
            if piro >= dungeons[y][0]:  # 현재 피로도가 최소 필요 피로도 이상일 때,
                piro -= dungeons[y][1]  # 현재 피로도를 소모 피로도만큼 감소
                pre_result += 1         # 던전 수 + 1
            else:      # 현재 피로도가 최소 피로도보다 작을 시,
                break  # 현재 반복문 탈출
            result = max(result, pre_result)  # 유저가 탐험할 수 있는 최대 던전 수

    return result

if __name__ == '__main__':
    print(solution(80, [[80, 20], [50, 40], [30, 10]]))  # 3
    print(solution(40, [[40, 20], [10, 10], [10, 10], [10, 10], [10, 10]]))  # 4