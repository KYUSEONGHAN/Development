# boj, 2217 : 로프, python3
import sys

N = int(sys.stdin.readline())
w = [int(sys.stdin.readline()) for i in range(N)]

w.sort()
w.reverse()

result = [w[i]*(i+1) for i in range(N)]

print(max(result))