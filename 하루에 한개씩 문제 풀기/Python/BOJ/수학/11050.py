# boj, 11050 : 이항 계수 1, python3
import sys

def multiply(arr):
    ans = 1
    for n in arr:
        if n == 0:
            return 0
        ans *= n
    return ans

def list_sort(num):
    return sorted(range(1, num + 1), reverse = True)

def binomial_coefficient(n, k):
    return multiply(list_sort(n)) // (multiply(list_sort(k)) * multiply(list_sort(n - k)))

N, K = map(int, sys.stdin.readline().split())

print(binomial_coefficient(N, K))