# boj, 2292 : 벌집, python3
import sys

N = int(sys.stdin.readline())

honeycomb = 1
cnt = 1

while N > honeycomb:
    honeycomb += 6 * cnt
    cnt += 1

print(cnt)