# boj, 11653 : 소인수분해, python3
import sys

N = int(sys.stdin.readline())
num = 2

while True:
    if N % num is 0:
        print(num)
        N //= num
    elif N is 1:
        break
    else:
        num += 1