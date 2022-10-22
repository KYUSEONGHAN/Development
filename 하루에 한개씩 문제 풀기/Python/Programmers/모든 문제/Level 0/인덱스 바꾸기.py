# https://school.programmers.co.kr/learn/courses/30/lessons/120895
# programmers, level0: 인덱스 바꾸기, python3
def solution(my_string: str, num1: int, num2: int) -> str:
    var1, var2 = my_string[num1], my_string[num2]
    string = list(my_string)
    string[num1], string[num2] = var2, var1

    return ''.join(string)

if __name__ == '__main__':
    print(solution("hello", 1, 2))
    print(solution("I love you", 3, 6))