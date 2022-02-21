# https://www.acmicpc.net/problem/12852
# boj, 12852: 1로 만들기 2, python3
import sys

input = sys.stdin.readline

def dp(n):
    # dp table 초기화
    d = [0] * 1000001
    # N을 1로 만드는 방법에 포함되어 있는 수를 나타내기위한 table 초기화
    result = [0] * 1000001
    result[1] = [1]

    # dp bottom-up
    for i in range(2, n+1):
        # 1을 빼는 경우
        d[i] = d[i-1] + 1
        result[i] = result[i-1] + [i]
        # x가 2로 나누어 떨어지면, 2로 나누는 경우
        if i % 2 == 0 and d[i//2] + 1 < d[i]:
            d[i] = d[i//2]+1
            result[i] = result[i//2] + [i]
        # x가 3으로 나누어 떨어지면, 3으로 나누는 경우
        if i % 3 == 0 and d[i//3] + 1 < d[i]:
            d[i] = d[i//3]+1
            result[i] = result[i//3] + [i]

    print(d[n])
    print(*sorted(result[n], reverse=True))

if __name__ == '__main__':
    n = int(input())

    dp(n)
