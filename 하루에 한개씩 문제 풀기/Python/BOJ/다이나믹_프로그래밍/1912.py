# boj, 1912 : 연속합, python3
import sys

n = int(sys.stdin.readline())

if n > 1000000 or n < 1:
    print("n range error")
else:
    num = list(map(int,sys.stdin.readline().split()))
    if len(num) != n:
        print("error")
    else:
        result = [0] * n
        result[0] = num[0]
        for i in range(1, n):
            result[i] = max(num[i], num[i]+result[i-1])
        print(max(result))
