# https://school.programmers.co.kr/learn/courses/30/lessons/120864
# programmers, level0: 숨어있는 숫자의 덧셈 (2), python3
def solution(my_string: str) -> int:
    answer = 0
    num = ''

    for x in my_string:
        if x.isdigit():
            num += x
        else:
            if num:
                answer += int(num)
                num = ''

    if num.isdigit():
        answer += int(num)

    return answer

if __name__ == '__main__':
    print(solution("aAb1B2cC34oOp"))  # 37
    print(solution("1a2b3c4d123Z"))   # 133