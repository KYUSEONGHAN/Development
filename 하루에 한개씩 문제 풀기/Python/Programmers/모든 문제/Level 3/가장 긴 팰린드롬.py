# https://school.programmers.co.kr/learn/courses/30/lessons/12904
# programmers, level3: 가장 긴 팰린드롬, python3
def check_palindrome(word: str) -> bool:
    return True if word == word[::-1] else False

def solution(s: str) -> int:
    answer = 0

    for x in range(len(s)):
        for y in range(x+1, len(s)+1):
            if check_palindrome(s[x:y]):
                answer = max(answer, y-x)

    return answer

if __name__ == '__main__':
    print(solution("abcdcba"))  # 7
    print(solution("abacde"))   # 3