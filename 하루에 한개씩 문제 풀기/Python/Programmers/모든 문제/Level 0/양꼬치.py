# https://school.programmers.co.kr/learn/courses/30/lessons/120830
# programmers, level0: 양꼬치, python3
def solution(n: int, k: int) -> int:
    return 12000 * n + 2000 * k - (n//10 * 2000)

if __name__ == '__main__':
    print(solution(10, 3))  # 124,000
    print(solution(64, 6))  # 768,000