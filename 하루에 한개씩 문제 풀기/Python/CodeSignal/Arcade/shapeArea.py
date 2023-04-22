def solution(n: int) -> int:
    dp = [0] * (n + 1)  # dp table
    dp[1] = 1

    # dp bottom-up
    for x in range(2, n + 1):
        dp[x] = dp[x - 1] + (4 * (x - 1))

    return dp[n]