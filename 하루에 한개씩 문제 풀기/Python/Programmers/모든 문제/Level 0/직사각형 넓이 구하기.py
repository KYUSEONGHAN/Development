# https://school.programmers.co.kr/learn/courses/30/lessons/120860
# programmers, level0: 직사각형 넓이 구하기, python3
def solution(dots: list) -> int:
    sorted_dots = sorted(dots, key=lambda x: (x[0], x[1]))
    x_length = sorted_dots[2][0] - sorted_dots[0][0]
    y_length = sorted_dots[1][1] - sorted_dots[0][1]

    return x_length * y_length

if __name__ == '__main__':
    print(solution([[1, 1], [2, 1], [2, 2], [1, 2]]))  # 1
    print(solution([[-1, -1], [1, 1], [1, -1], [-1, 1]]))  # 4