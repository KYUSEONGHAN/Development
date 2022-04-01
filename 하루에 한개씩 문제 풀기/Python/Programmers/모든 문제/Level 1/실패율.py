# https://programmers.co.kr/learn/courses/30/lessons/42889
# programmers, level1: 실패율, python3
def solution(N: int, stages: list) -> list:
    lenth = len(stages)
    answer = []

    # n번만큼 반복
    for x in range(1, N+1):
        # cnt: 클리어하지 못한 유저 수
        cnt = 0
        for data in stages:
            if x == data:
                cnt += 1
        # 런타임 에러를 피하기위해 if else문 처리
        answer.append([cnt / lenth, x]) if lenth != 0 else answer.append([0, x])
        lenth -= cnt

    # answer에 있는값을 실패율 순으로 내림차순 정렬
    # 이 때, 실패율이 같다면 낮은 번호대로 내림차순 정렬하도록 lambda 사용
    # 번호만 반환하도록 -1인덱스 추출
    return [rate[-1] for rate in sorted(answer, reverse=True, key=lambda x: (x[0], -x[1]))]

if __name__ == '__main__':
    print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))  # [3,4,2,1,5]
    print(solution(4, [4, 4, 4, 4, 4]))   # [4,1,2,3]