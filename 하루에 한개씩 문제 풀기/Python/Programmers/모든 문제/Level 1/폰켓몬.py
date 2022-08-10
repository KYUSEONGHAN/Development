# https://school.programmers.co.kr/learn/courses/30/lessons/1845
# programmers, level1: 폰켓몬, python3
def solution(nums: list) -> int:
    return min(len(set(nums)), len(nums) // 2)

if __name__ == '__main__':
    print(solution([3, 1, 2, 3]))  # 2
    print(solution([3, 3, 3, 2, 2, 4]))  # 3
    print(solution([3, 3, 3, 2, 2, 2]))  # 2