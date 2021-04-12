# boj, 1546 : 평균, python3
import sys

N = int(sys.stdin.readline())

score = list(map(int,sys.stdin.readline().split()))
result = []

for i in range(N):
    if score[i] <= max(score):
        result.append(score[i]/max(score)*100)

print(sum(result)/N)
