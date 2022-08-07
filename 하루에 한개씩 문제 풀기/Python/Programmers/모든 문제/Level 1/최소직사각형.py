# https://school.programmers.co.kr/learn/courses/30/lessons/86491
# programmers, level1: 최소직사각형, python3
def solution(sizes: list) -> int:
    rearrange, max_x, max_y = [], 0, 0

    for size in sizes:  # 더 큰 값을 첫번째 인덱스로, 작은값을 두번째 인덱스로 재배열
        if size[0] >= size[1]:
            rearrange.append([size[0], size[1]])
        else:
            rearrange.append([size[1], size[0]])

    for x in rearrange:
        max_x, max_y = max(x[0], max_x), max(x[1], max_y)

    return max_x * max_y


if __name__ == '__main__':
    print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))  # 4000
    print(solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]))  # 120
    print(solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]))  # 133