# https://school.programmers.co.kr/learn/courses/30/lessons/120840
# programmers, level0: 구슬을 나누는 경우의 수, python3
def factorial(num: int) -> int:
    if num == 0:
        return 1
    if num <= 2:
        return num
    return factorial(num-1) * num

def solution(balls: int, share: int) -> int:
    return factorial(balls) // (factorial(balls-share) * factorial(share))

if __name__ == '__main__':
    print(solution(3, 2))  # 3
    print(solution(5, 3))  # 10
    print(solution(5, 5))