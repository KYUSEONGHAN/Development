# boj, 11053 : 가장 긴 증가하는 부분 수열, python
# dp : 큰 문제를 작은 문제로 나눠서 푸는 알고리즘
import sys

def DP(A):
    for i in range(N):
        for j in range(i):
            if all((A[i] > A[j], d[i] < d[j])):
                d[i] = d[j]
        d[i] += 1
    return max(d)

N = int(sys.stdin.readline())
A = list(map(int, input().split()))
d = [0] * N

print(DP(A))