# boj, 1764 : 듣보잡, python3
import sys

N, M = map(int,input().split())
#N, M = map(int,sys.stdin.readline().split())

listen = []
see = []

for i in range(N):
    listen.append(str(input()))
    #listen.append(str(sys.stdin.readline()))
for i in range(M):
    see.append(str(input()))
    #see.append(str(sys.stdin.readline()))

result = list(sorted(set(listen).intersection(see)))

print(len(result))
print("\n".join(result))