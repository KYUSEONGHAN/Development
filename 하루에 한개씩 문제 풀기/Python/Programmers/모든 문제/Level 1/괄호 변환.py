# https://school.programmers.co.kr/learn/courses/30/lessons/60058
# programmers, level1: 괄호 변환, python3

# 1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다.
def phase1(word: str) -> bool:
    return True if word else False

# 2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다. 단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며, v는 빈 문자열이 될 수 있습니다.
def phase2(word: str):
    count = 0

    for index, x in enumerate(word):
        if x == '(':
            count += 1
        else:
            count -= 1
        if count == 0:
            return word[:index+1], word[index+1:]

# 3. 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행합니다.
#   3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다.
def phase3(word: str) -> bool:
    count = 0

    for x in word:
        if x == '(':
            count += 1
        else:
            count -= 1
        if count < 0:
            return False

    return True if count == 0 else False

# 4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다.
#   4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다.
#   4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다.
#   4-3. ')'를 다시 붙입니다.
#   4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다.
#   4-5. 생성된 문자열을 반환합니다.
def phase4(u: str, v: str) -> str:
    answer = '('
    answer += solution(v)
    answer += ')'

    for x in u[1:-1]:
        if x == '(':
            answer += ')'
        else:
            answer += '('

    return answer

def solution(p: str) -> str:
    if not phase1(p):
        return ''

    u, v = phase2(p)

    return u + solution(v) if phase3(u) else phase4(u, v)

if __name__ == '__main__':
    print(solution("(()())()"))   # "(()())()"
    print(solution(")("))         # "()"
    print(solution("()))((()"))   # "()(())()"