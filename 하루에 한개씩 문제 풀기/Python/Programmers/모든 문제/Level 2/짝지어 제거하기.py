# https://school.programmers.co.kr/learn/courses/30/lessons/12973
# programmers, level2: 짝지어 제거하기, python3

# 무한반복문과 슬라이싱을 이용한 순수 구현 버전
# def solution(s: str) -> int:
#     start, length = 0, len(s)
#
#     if length % 2 == 1:
#         return 0
#
#     while True:
#         if s[start] == s[start+1]:
#             s = s[:start] + s[start+2:]
#             start = 0
#         else:
#             start += 1
#         if not s or start + 1 >= length:
#             break
#
#     return 1 if not s else 0

# stack을 활용한 구현 버전
def solution(word: str) -> int:
    if len(word) % 2 == 1:
        return 0

    stack = [word[0]]

    for x in range(1, len(word)):
        if not stack:
            stack.append(word[x])
            continue

        alpha = stack[-1]

        if alpha == word[x]:
            stack.pop()
        else:
            stack.append(word[x])

    return 1 if not stack else 0

if __name__ == '__main__':
    print(solution('baabaa'))      # 1
    print(solution('cdcd'))        # 0
    print(solution("abccba"))      # 1
    print(solution("abcccba"))     # 0
    print(solution("abccccbaaa"))  # 1
    print(solution("abccaabaa"))   # 0
    print(solution("a"))           # 0