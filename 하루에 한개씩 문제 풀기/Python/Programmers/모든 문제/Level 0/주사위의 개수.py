# https://school.programmers.co.kr/learn/courses/30/lessons/120845
# programmer, level0: 주사위의 개수, python3
def multi(nums: list) -> int:
    result = 0

    for x in nums:
        if not result:
            result = x
            continue
        result *= x

    return result

def solution(box: list, n: int) -> int:
    return multi([x//n for x in box])

if __name__ == '__main__':
    print(solution([1, 1, 1], 1))    # 1
    print(solution([10, 8, 6], 3))   # 12