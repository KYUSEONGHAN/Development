# https://programmers.co.kr/skill_checks/385791?challenge_id=2549
# programmers, 스킬 체크 테스트 Level2: 문제 2, python3
def solution(citations: list) -> int:
    citations = sorted(citations, reverse=True)  # 내림차순 정렬
    answer = 0

    for i in range(len(citations)):
        if i + 1 <= citations[i]:
            answer = i + 1
        else:
            break

    return answer

if __name__ == '__main__':
    print(solution([3, 0, 6, 1, 5]))  # 3