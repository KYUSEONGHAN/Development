# https://school.programmers.co.kr/learn/courses/30/lessons/92335
# programmers, 2022 kakao blind recuit, level2: k진수에서 소수 개수 구하기, python3
import math

# 10진수 n을 k진수로 변환하는 함수
def convert_binary(n: int, k: int) -> str:
    arr = []

    while n:
        r = n % k
        n = n // k
        arr.append(r)

    return ''.join(list(map(str, arr[::-1])))

# 주어진 수가 소수인지 체크하는 함수
def check_sosu(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n) + 1)):  # 2부터 x의 제곱근까지의 숫자
        if n % i == 0:  # 나눠떨어지는 숫자가 있으면 소수가 아님
            return False
    return True  # 전부 나눠떨어지지 않는다면 소수임

# main 함수
def solution(n: int, k: int) -> int:
    answer = 0

    binary = convert_binary(n, k)

    # '0'을 기준으로 split 분할
    # for 반복문으로 순차 조회
    for x in binary.split('0'):
        # 현재 요소가 '' 값이 아니고 소수이면 증감
        if x:
            if check_sosu(int(x)):
                answer += 1

    return answer

if __name__ == '__main__':
    print(solution(437674, 3))  # 3
    print(solution(110011, 10))  # 2