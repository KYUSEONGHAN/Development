# https://school.programmers.co.kr/learn/courses/30/lessons/120585
# programmers, level0: 머쓱이보다 키 큰 사람, python3
def solution(array: list, height: int):
    return sum([1 for x in array if x > height])

if __name__ == '__main__':
    print(solution([149, 180, 192, 170], 167))  # 3
    print(solution([180, 120, 140], 190))       # 0