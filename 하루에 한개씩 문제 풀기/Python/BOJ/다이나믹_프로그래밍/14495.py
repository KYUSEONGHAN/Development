# https://www.acmicpc.net/problem/14495
# boj, 14495: 피보나치 비스무리한 수열, python3
def fibonacci(num: int) -> int:
    dp = [0] * 117  # dp table 초기화
    dp[1], dp[2], dp[3] = 1, 1, 1

    # dp bottom-up
    for x in range(4, num+1):
        dp[x] = dp[x-1] + dp[x-3]

    return dp[num]

if __name__ == '__main__':
    # 자연수 n(1 ≤ n ≤ 116)이 주어진다.
    n = int(input())

    # n번째 피보나치 비스무리한 수를 출력한다.
    print(fibonacci(n))