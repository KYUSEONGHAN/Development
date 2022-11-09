# https://school.programmers.co.kr/learn/courses/30/lessons/120846
# programmers, level0: 합성수 찾기, python3
def solution(n: int) -> int:
    result = 0

    for x in range(4, n+1):
        num = 0
        for y in range(1, x+1):
            if num == 2:
                result += 1
                break
            if x % y == 0:
                num += 1

    return result

if __name__ == '__main__':
    print(solution(10))  # 5
    print(solution(15))  # 8