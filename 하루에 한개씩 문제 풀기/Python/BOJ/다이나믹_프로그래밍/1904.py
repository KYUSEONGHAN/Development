# acmicpc.net/problem/1904
# boj, 1904: 01타일, python3
import sys

input = sys.stdin.readline  # 변수 입력 속도 향상

# 지원이가 만들 수 있는 길이가 n인 모든 2진 수열의 개수를 반환하는 함수
def solve(n: int) -> int:
    d = [0] * 1000001  # dp table 초기화
    d[1], d[2] = 1, 2

    # dp bottom-up
    for i in range(3, n+1):
        d[i] = (d[i-1] + d[i-2]) % 15746  # 수열의 개수를 15746으로 나눈 나머지를 반환

    return d[n]

if __name__ == '__main__':
    n = int(input())

    print(solve(n))