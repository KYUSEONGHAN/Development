# boj, 13410 : 거꾸로 구구단, python3
# 브루트포스 알고리즘
import sys

def reverse_gugudan(n,k):
    return max([int(str(n*i)[::-1]) for i in range(1, k+1)])

N, K = map(int, sys.stdin.readline().split())

print(reverse_gugudan(N,K))