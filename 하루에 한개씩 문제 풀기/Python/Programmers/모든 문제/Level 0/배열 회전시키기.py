# https://school.programmers.co.kr/learn/courses/30/lessons/120844
# programmers, level0: 배열 회전시키기, python3
def solution(numbers: list, direction: str) -> list:
    return numbers[1:] + [numbers[0]] if direction == 'left' else [numbers[-1]] + numbers[:-1]

if __name__ == '__main__':
    print(solution([1, 2, 3], "right"))  # [3, 1, 2]
    print(solution([4, 455, 6, 4, -1, 45, 6], "left"))  # [455, 6, 4, -1, 45, 6, 4]