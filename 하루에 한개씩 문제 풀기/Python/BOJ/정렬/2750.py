# boj, 2750 : 수 정렬하기, python3
N = int(input())

num = []

for _ in range(N):
    num.append(int(input()))

num.sort()

for i in num:
    print(i)

#(sol2)
N = int(input())

num = []

for _ in range(N):
    num.append(int(input()))

for i in range(len(num)):
    for j in range(len(num)):
        if num[i] < num[j]:
            num[i], num[j] = num[j], num[i]

for n in num:
    print(n)