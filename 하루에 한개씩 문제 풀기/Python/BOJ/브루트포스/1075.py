# https://www.acmicpc.net/problem/1075
# boj, 1075: 나누기, python3
import sys

input = sys.stdin.readline  # 변수 입력 속도 향상

# n의 가장 뒤 두 자리를 적절히 바꿔서 n을 f로 나누어 떨어지게 만드는 함수
def solve(n: int, f: int) -> str:
    n = str(n)[:-2] + '00'  # n을 슬라이싱하기 위해 string 형변환을 한 뒤, 가장 뒤 두 자리수를 00으로 변환

    while True:    # 무한반복문
        if int(n) % f == 0:  # 만약 n이 f로 나누어 떨어진다면
            return n[-2:]    # 현재 n의 가장 뒤 두 자리수를 반환
        n = str(int(n) + 1)  # 그렇지 않다면 +1

if __name__ == '__main__':
    n = int(input())
    f = int(input())

    print(solve(n, f))