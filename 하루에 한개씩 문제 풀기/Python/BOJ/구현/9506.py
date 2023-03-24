# https://www.acmicpc.net/problem/9506
# boj, 9506: 약수들의 합, python3
import sys

input = sys.stdin.readline

# 약수 반환해주는 함수
def get_yaksu(n: int) -> list:
    return [x for x in range(1, n) if n % x == 0]

# 완전수인지 체크해주는 함수
def check_perfect_num(n: int, l: list) -> bool:
    return True if n == sum(l) else False

# main solution 함수
def solve(n: int):
    yaksu = get_yaksu(n)

    # 완전수일경우
    if check_perfect_num(n, yaksu):
        return f'{n} = ' + ' + '.join(str(x) for x in yaksu)

    return f'{n} is NOT perfect.'

if __name__ == '__main__':
    while True:
        n = int(input())

        if n == -1:
            break

        print(solve(n))