import sys

baduk = [[0 for j in range(20)] for i in range(20)]
cnt = 0

for i in range(19):
    badukal = list(map(int, sys.stdin.readline().split()))
    for j in range(19):
        baduk[i + 1][j + 1] = badukal[j]

n = int(input())

for _ in range(n):
    cross = list(map(int, sys.stdin.readline().split()))
    for i in range(1, 20):
        if baduk[cross[0]][i] == 0:
            baduk[cross[0]][i] = 1
        else:
            baduk[cross[0]][i] = 0
        if baduk[i][cross[1]] == 0:
            baduk[i][cross[1]] = 1
        else:
            baduk[i][cross[1]] = 0

for i in range(1, 20):
    for j in range(1, 20):
        print(baduk[i][j], end=' ')
    print('')