# boj, 2751 : 수 정렬하기2, python3
N = int(input())
num = []

for i in range(N):
    num.append(int(input()))

num = sorted(set(num))

for i in num:
    print(i)
