# https://school.programmers.co.kr/learn/courses/30/lessons/136798
# programmers, level1: 기사단원 무기, python3
def get_num_divisor(num: int) -> int:  # 약수 개수 구하는 함수
    divisor_num = 0

    for i in range(1, int(num ** (1 / 2)) + 1):
        if (num % i == 0):
            divisor_num += 1
            if ((i ** 2) != num):
                divisor_num += 1

    return divisor_num

def solution(number: int, limit: int, power: int) -> int:
    answer = 0

    for x in range(1, number+1):
        divisor_num = get_num_divisor(x)
        # 현재 반복문 요소의 약수 개수가 공격력 제한 수치를 넘지 않을시,
        if divisor_num <= limit:
            answer += divisor_num
        # 현재 반복문 요소의 약수 개수가 공격력 제한 수치를 넘으면 -> 협약기관에서 정한 공격력으로 대체
        else:
            answer += power

    return answer

if __name__ == '__main__':
    print(solution(5, 3, 2))   # 10
    print(solution(10, 3, 2))  # 21