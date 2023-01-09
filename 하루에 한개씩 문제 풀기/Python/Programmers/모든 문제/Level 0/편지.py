# https://school.programmers.co.kr/learn/courses/30/lessons/120898
# programmers, level0: 편지, python3
def solution(message: str) -> int:
    return len(message) * 2

if __name__ == '__main__':
    print(solution("happy birthday!"))  # 30
    print(solution("I love you~"))  # 22