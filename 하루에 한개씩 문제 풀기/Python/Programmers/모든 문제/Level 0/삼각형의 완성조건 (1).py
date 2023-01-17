# https://school.programmers.co.kr/learn/courses/30/lessons/120889
# programmers, level0: 삼각형의 완성조건 (1), python3
def solution(sides: list) -> int:
    sort_sides = sorted(sides)
    return 1 if sort_sides[0] + sort_sides[1] > sort_sides[2] else 2

if __name__ == '__main__':
    print(solution([1, 2, 3]))  # 2
    print(solution([3, 6, 2]))  # 2
    print(solution([199, 72, 222]))  # 1