# boj, 1110 : 더하기 사이클, python3
N = int(input())
cnt = 0
num = N

while True:
    num_1 = num//10
    num_2 = num%10
    num_3 = (num_1+num_2)%10
    num = (num_2*10)+num_3
    cnt += 1
    if num == N:
        print(cnt)
        break