# https://www.acmicpc.net/problem/9461
# boj, 9461: 파도반 수열, python3
import sys

input = sys.stdin.readline  # 변수 입력 속도 향상

# p(n)을 구하는 함수
def solve(n: int) -> int:
    d = [0] * 101  # dp table 초기화
    d[1], d[2], d[3] = 1, 1, 1

    # dp bottom-up
    for i in range(4, n+1):
        d[i] = d[i-2] + d[i-3]

    return d[n]  # P(N) 반환

if __name__ == '__main__':
    t = int(input())  # 테스트 케이스의 개수 t

    for _ in range(t):   # 각 테스트 케이스마다 P(n)을 출력한다.
        n = int(input())
        print(solve(n))