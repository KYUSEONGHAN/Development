# https://school.programmers.co.kr/learn/courses/30/lessons/120907
# programmers, level0: OX퀴즈, python3
def plus(num1: int, num2: int) -> str:
    return str(num1 + num2)

def minus(num1: int, num2: int) -> str:
    return str(num1 - num2)

def solution(quiz: list) -> list:
    answer = []

    for x in quiz:
        num1, operator, num2, _, result = x.split()
        if operator == '+':
            tmp = plus(int(num1), int(num2))
        else:
            tmp = minus(int(num1), int(num2))

        if tmp == result:
            answer.append('O')
        else:
            answer.append('X')

    return answer

if __name__ == '__main__':
    print(solution(["3 - 4 = -3", "5 + 6 = 11"]))  # ["X", "O"]
    print(solution(["19 - 6 = 13", "5 + 66 = 71", "5 - 15 = 63", "3 - 1 = 2"]))  # ["O", "O", "X", "O"]