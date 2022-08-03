# https://school.programmers.co.kr/learn/courses/30/lessons/12980
# programmers, level2: 점프와 순간 이동, python3
def solution(n: int) -> int:
    jump = 0

    while n != 0:       # n을 거꾸로부터 추적
        if n % 2 == 0:  # n이 2로 나누어 떨어지면
            n //= 2     # 2로 나눔 -> 순간이동
        else:
            n -= 1
            jump += 1   # 1칸 jump

    return jump

if __name__ == '__main__':
    print(solution(5))      # 2
    print(solution(6))      # 2
    print(solution(5000))   # 5