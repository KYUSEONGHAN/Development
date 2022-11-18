# https://school.programmers.co.kr/learn/courses/30/lessons/120912
# programmer, level0: 7의 개수, python3
def solution(array: list) -> int:
    return sum([str(x).count('7') for x in array])

if __name__ == '__main__':
    print(solution([7, 77, 17]))  # 4
    print(solution([10, 29]))     # 0