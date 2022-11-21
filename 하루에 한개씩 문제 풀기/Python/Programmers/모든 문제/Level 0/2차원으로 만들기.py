# https://school.programmers.co.kr/learn/courses/30/lessons/120842
# programmers, level0: 2차원으로 만들기, python3
def solution(num_list: list, n: int) -> list:
    return [num_list[x:x+n] for x in range(0, len(num_list), n)]

if __name__ == '__main__':
    print(solution([1, 2, 3, 4, 5, 6, 7, 8], 2))
    print(solution([100, 95, 2, 4, 5, 6, 18, 33, 948], 3))