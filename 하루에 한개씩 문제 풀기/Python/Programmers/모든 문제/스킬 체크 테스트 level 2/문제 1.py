# https://programmers.co.kr/skill_checks/385791
# programmers, 스킬 체크 테스트 leve 2: 문제 1, python3

# n번째 피보나치 수를 1234567으로 나눈 나머지를 리턴하는 함수
def solution(n):
    d = [0] * (100001)  # dp table 초기화
    d[1] = 1

    # dp bottom-up
    for i in range(2, n+1):
        d[i] = (d[i-2] + d[i-1]) % 1234567

    return d[n]

if __name__ == '__main__':
    print(solution(3))  # 2
    print(solution(5))  # 5