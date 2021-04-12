# boj, 1427 : 소트인사이드, python3
import sys

#N = list(map(str,input()))
N = list(map(str,sys.stdin.readline()))

result = []

for i in N:
    result.append(i)

result.sort()
result.reverse()

print(''.join(result))