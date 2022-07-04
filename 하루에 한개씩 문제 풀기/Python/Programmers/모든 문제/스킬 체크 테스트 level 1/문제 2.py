# https://programmers.co.kr/skill_checks/385768?challenge_id=953
# programmers, 스킬 체크 테스트 level1: 문제 2, python3

# 배열 arr의 평균값을 return하는 함수
def solution(arr: list):
    return sum(arr) / len(arr)

if __name__ == '__main__':
    print(solution([1, 2, 3, 4]))  # 2.5
    print(solution([5, 5]))        # 5