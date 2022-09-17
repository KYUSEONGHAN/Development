# https://school.programmers.co.kr/learn/courses/30/lessons/76502
# programmers, level2: 괄호 회전하기, python3
from collections import deque

# 옳바른 괄호인지 체크하는 함수
def bracket_check(queue: deque) -> bool:
    stack = []

    for x in queue:
        if x == '(' or x == '[' or x == '{':
            stack.append(x)
        elif x == ')':
            if stack:
                bracket = stack.pop()
                if bracket != '(':
                    return False
            else:
                return False
        elif x == ']':
            if stack:
                bracket = stack.pop()
                if bracket != '[':
                    return False
            else:
                return False
        elif x == '}':
            if stack:
                bracket = stack.pop()
                if bracket != '{':
                    return False
            else:
                return False

    return True if not stack else False

def solution(s: str) -> int:
    answer, cnt = 0, 0  # cnt: 반복문 수행에 쓰일 변수
    queue = deque(s)  # input string data를 queue에 할당

    if len(s) % 2 != 0:  # 주어진 문자열의 길이가 짝수가 아닌 경우 올바른 괄호 문자열에 해당하지 않으므로 0 반환
        return 0

    # 문자열의 길이만큼 반복문 수행
    while cnt != len(s):
        if bracket_check(queue):
            answer += 1

        x = queue.popleft()
        queue.append(x)
        cnt += 1

    return answer

if __name__ == '__main__':
    print(solution("[](){}"))  # 3
    print(solution("}]()[{"))  # 2
    print(solution("[)(]"))    # 0
    print(solution("}}}"))     # 0
    print(solution("([{)}]"))  # 0
