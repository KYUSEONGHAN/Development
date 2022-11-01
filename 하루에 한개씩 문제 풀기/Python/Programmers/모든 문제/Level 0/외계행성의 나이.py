# https://school.programmers.co.kr/learn/courses/30/lessons/120834
# programmers, level0: 외계행성의 나이, python3
def solution(age: int) -> str:
    dict = {index: chr(x) for index, x in enumerate(range(97, 97+10))}

    return ''.join(map(str, [dict[int(x)] for x in list(str(age))]))

if __name__ == '__main__':
    print(solution(23))   # "cd"
    print(solution(51))   # "fb"
    print(solution(100))  # "baa"