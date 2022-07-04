# https://programmers.co.kr/skill_checks/385768
# programmers, 스킬 체크 테스트 level1: 문제 1, python3
def solution(num: int) -> str:
    return "Odd" if num % 2 == 1 else 'Even'

if __name__ == '__main__':
    print(solution(3))
    print(solution(4))