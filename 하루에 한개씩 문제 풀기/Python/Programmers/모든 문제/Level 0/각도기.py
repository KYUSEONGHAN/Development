# https://school.programmers.co.kr/learn/courses/30/lessons/120829
def solution(angle: int) -> int:
    if angle < 90:
        return 1
    elif angle == 90:
        return 2
    elif angle > 90 and angle < 180:
        return 3
    elif angle == 180:
        return 4

if __name__ == '__main__':
    print(solution(70))   # 1
    print(solution(91))   # 3
    print(solution(180))  # 4