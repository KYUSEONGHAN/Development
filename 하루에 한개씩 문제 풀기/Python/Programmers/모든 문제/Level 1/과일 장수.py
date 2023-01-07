# https://school.programmers.co.kr/learn/courses/30/lessons/135808
# programmers, level1: 과일 장수, python3
def solution(k: int, m: int, score: list) -> int:
    answer = 0
    # score 내림차순으로 재정렬
    sort_score = sorted(score, reverse=True)
    # m개씩 분할
    split_score = [sort_score[x:x+m] for x in range(0, len(sort_score), m)]
    # 가격 측정
    for x in split_score:
        if len(x) >= m:
            answer += x[-1] * m

    return answer

if __name__ == '__main__':
    print(solution(3, 4, [1, 2, 3, 1, 2, 3, 1]))  # 8
    print(solution(4, 3, [4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2]))  # 33