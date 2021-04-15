# boj, 2908 : 상수, python3
import sys

A, B = map(int, sys.stdin.readline().split())
a_list = list(map(int, str(A)))
b_list = list(map(int, str(B)))

a_list.reverse()
b_list.reverse()

a_merge = ''
b_merge = ''

for i in a_list:
    a_merge += str(i)
for i in b_list:
    b_merge += str(i)

print(max(int(a_merge), int(b_merge)))