import sys

n = int(sys.stdin.readline())
bunho_list = list(map(int,sys.stdin.readline().split()))
num_list = [i for i in range(1,23+1)]
result = [0 for i in range(1,23+1)]

for i in num_list:
    for j in bunho_list:
        if i == j:
            result[i-1] += 1

print(" ".join(map(str,result)))