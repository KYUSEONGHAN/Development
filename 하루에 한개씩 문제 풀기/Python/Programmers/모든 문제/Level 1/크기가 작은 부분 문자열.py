# https://school.programmers.co.kr/learn/courses/30/lessons/147355
# programmers, level1: 크기가 작은 부분 문자열, python3
def solution(t: str, p: str) -> int:
    return sum([1 for x in range(len(t) - len(p) + 1) if int(p) >= int(t[x:x+len(p)])])

if __name__ == '__main__':
    print(solution("3141592", "271"))  # 2
    print(solution("500220839878", "7"))  # 8
    print(solution("10203", "15"))  # 3