# boj, 10814 : 나이순 정렬, python3
import sys

N = int(sys.stdin.readline())
age_name = []

for i in range(N):
    a_n = list(map(str, sys.stdin.readline().split()))
    a_n[0] = int(a_n[0])
    age_name.append(a_n)

age_name.sort(key=lambda x: (x[0]))

for i in age_name:
    print(i[0], i[1])