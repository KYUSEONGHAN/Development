# boj, 1037 : 약수, python3
# 정수론 및 조합론
import sys

def solution(l):
    return l[0] * l[-1]

num = int(sys.stdin.readline())
n_list = sorted(map(int, sys.stdin.readline().split()))

print(solution(n_list))