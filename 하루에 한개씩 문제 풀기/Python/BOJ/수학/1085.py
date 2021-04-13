# boj, 1085 : 직사각형에서 탈출, python3
import sys
import math

x, y, w, h = map(int,sys.stdin.readline().split())

result = []
result.append(w-x)
result.append(h-y)
result.append(math.sqrt((w-x)**2+(h-y)**2))
result.append(math.sqrt((x)**2+(y)**2))
result.append(x)
result.append(y)

print(min(result))