# https://school.programmers.co.kr/learn/courses/30/lessons/120906
# programmers,level0: 자릿수 더하기, python3
def solution(n: int) -> int:
    return sum([int(x) for x in str(n)])

if __name__ == '__main__':
    print(solution(1234))    # 10
    print(solution(930211))  # 16