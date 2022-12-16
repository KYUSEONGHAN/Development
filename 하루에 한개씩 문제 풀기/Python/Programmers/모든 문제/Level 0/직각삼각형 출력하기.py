# https://school.programmers.co.kr/learn/courses/30/lessons/120823
# programmers, level0: 직각삼각형 출력하기, python3
def solve(n: int):
    for x in range(1, n+1):
        print('*' * x)

if __name__ == '__main__':
    n = int(input())

    solve(n)