# 1026번
import sys

def bomul(A, B):
    return sum(a * b for a, b in zip(sorted(A), sorted(B, reverse = True)))


N = int(sys.stdin.readline())
A = list(map(int, sys.stidn.readline().split()))
B = list(map(int, sys.stdin.readline().split()))


print(bomul(A, B))

# 최적 코드 -> 윤상님 코드

n = int(input())

a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))

s = 0
for i in range(n):
    s += min(a_list) * max(b_list)
    a_list.pop(a_list.index(min(a_list)))
    b_list.pop(b_list.index(max(b_list)))

print(s)