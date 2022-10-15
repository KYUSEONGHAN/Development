# https://school.programmers.co.kr/learn/courses/30/lessons/120841
# programmers, level0: 점의 위치 구하기, python3
def solution(dot: list) -> int:
    x, y, answer = dot[0], dot[-1], 0

    if x > 0 and y > 0:
        return 1
    elif x < 0 and y > 0:
        return 2
    elif x < 0 and y < 0:
        return 3
    else:
        return 4

if __name__ == '__main__':
    print(solution([2, 4]))   # 1
    print(solution([-7, 9]))  # 2