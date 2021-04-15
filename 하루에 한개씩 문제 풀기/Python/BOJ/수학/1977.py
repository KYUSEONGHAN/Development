# boj, 1977 : 완전제곱수, python3
import sys
import math

M = int(sys.stdin.readline())
N = int(sys.stdin.readline())
result = []

for i in range(M,N+1):
    root = str(math.sqrt(i)).split('.')
    if root[1] == '0':
        result.append(i)

if len(result) == 0:
    print(-1)
else:
    print(sum(result))
    print(min(result))
