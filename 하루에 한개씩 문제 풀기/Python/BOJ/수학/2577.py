# boj, 2577 : 숫자의 개수, python3
import sys

A = int(sys.stdin.readline())
B = int(sys.stdin.readline())
C = int(sys.stdin.readline())

num_list = [i for i in range(10)]
mul = A * B * C
nums = list(map(int, str(mul)))
result = [0 for i in range(10)]
cnt = 0

for i in num_list:
    for j in nums:
        if i == j:
            result[cnt] += 1
    cnt += 1

print("\n".join(map(str, result)))