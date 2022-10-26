# https://school.programmers.co.kr/learn/courses/30/lessons/120921
# programmers, level0: 문자열 밀기, python3
def solution(A: str, B: str) -> int:
    result = 0

    while result != len(A):
        if A == B:
            return result
        A = A[-1] + A[:-1]
        result += 1

    return -1

if __name__ == '__main__':
    print(solution("hello", "ohell"))   # 1
    print(solution("apple", "elppa"	))  # -1