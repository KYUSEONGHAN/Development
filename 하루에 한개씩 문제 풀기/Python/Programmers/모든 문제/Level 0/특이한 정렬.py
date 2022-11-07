# https://school.programmers.co.kr/learn/courses/30/lessons/120880
# programemrs, level0: 특이한 정렬, python3
def solution(numlist: list, n: int) -> list:
    return sorted(numlist, key=lambda x: (abs(n-x), -x))

if __name__ == '__main__':
    print(solution([1, 2, 3, 4, 5, 6], 4))              # [4, 5, 3, 6, 2, 1]
    print(solution([10000,20,36,47,40,6,10,7000], 30))  # [36, 40, 20, 47, 10, 6, 7000, 10000]