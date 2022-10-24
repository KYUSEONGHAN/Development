# https://programmers.co.kr/skill_checks/431248
# programmers, 스킬 체크 테스트 level3: 문제 1, python3
def isPalindrome(word: str) -> bool:
    return True if word == word[::-1] else False

def solution(s: str) -> int:
    result = 0

    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            if isPalindrome(s[i:j]):
                result = max(result, len(s[i:j]))

    return result


if __name__ == '__main__':
    print(solution("abcdcba"))  # 7
    print(solution("abacde"))   # 3