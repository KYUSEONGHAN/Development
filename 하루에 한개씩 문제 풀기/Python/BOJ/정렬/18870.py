# boj, 18870 : 좌표 압축, python3
import sys

def compression(N):
    x_list = list(map(int, input().split()))

    result = [sum(num < i for num in x_list) for i in x_list]

    return ' '.join(map(str, result))


N = int(input())

print(compression(N))


# 시간초과 코드2
import sys


def compression(N):
    x_list = list(map(int, input().split()))
    sort_list = sorted(x_list)

    result = [sort_list.index(i) for i in x_list]

    return ' '.join(map(str, result))


N = int(input())

print(compression(N))


# 성공 코드
import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

arr2 = sorted(list(set(arr)))
dic = {arr2[i]: i for i in range(len(arr2))}
for i in arr:
    print(dic[i], end=' ')