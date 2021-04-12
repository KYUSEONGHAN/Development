# boj, 4344 : 평균은 넘겠지, python3
import sys

C = int(sys.stdin.readline())
cnt = 0

for i in range(C):
    N_score = list(map(int, sys.stdin.readline().split()))
    average = sum(N_score[1:]) // N_score[0]

    for j in N_score[1:]:
        if average < j:
            cnt += 1
    print("%.3f%%" % ((cnt / N_score[0]) * 100))
    cnt = 0