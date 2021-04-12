# boj, 8958 : ox퀴즈, python3
import sys

T = int(sys.stdin.readline())

for t in range(T):
    quiz = list(map(str,input().split('X')))
    result = []

    for i in quiz:
        for j in range(1,len(i)+1):
            result.append(j)

    print(sum(result))