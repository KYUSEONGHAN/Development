# https://school.programmers.co.kr/learn/courses/30/lessons/120892
# programmers, level0: 암호 해독, python3
def solution(cipher: str, code: int) -> str:
    return ''.join(map(str, [x for index, x in enumerate(cipher, start=1) if index % code == 0]))

if __name__ == '__main__':
    print(solution("dfjardstddetckdaccccdegk", 4))
    print(solution("pfqallllabwaoclk", 2))