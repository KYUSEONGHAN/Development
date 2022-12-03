# https://school.programmers.co.kr/learn/courses/30/lessons/120903
# programmers, level0: 배열의 유사도, python3
def solution(s1: list, s2: list) -> int:
    return len(set(s1) & set(s2))

if __name__ == '__main__':
    print(solution(["a", "b", "c"], ["com", "b", "d", "p", "c"]))  # 2
    print(solution(["n", "omg"], ["m", "dot"]))  # 0