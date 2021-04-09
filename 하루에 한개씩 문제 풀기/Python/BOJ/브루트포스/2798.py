# boj, 2798 : 블랙잭, python3
N,M = map(int,input().split())

num = list(map(int,input().split()))
sum = []

if len(num)!=N:
    print("input data error")
else:
    for i in range(N):
        for j in range(i+1,N):
            for k in range(j+1,N):
                sum_index = num[i] + num[j] + num[k]
                if sum_index <= M:
                    sum.append(sum_index)
    print(max(sum))