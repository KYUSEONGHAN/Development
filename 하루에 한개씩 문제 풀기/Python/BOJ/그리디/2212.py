# boj, 2212 : 센서, python3
# 그리디 알고리즘
import sys


def sensor(n, k, l):
    sensor_list = sorted([l[i] - l[i - 1] for i in range(1, n)])

    for _ in range(k - 1):
        sensor_list.pop()

    return sum(sensor_list)


N = int(sys.stdin.readline())
K = int(sys.stdin.readline())
l = sorted(list(map(int, sys.stdin.readline().split())))

if N <= K:
    print(0)
else:
    print(sensor(N, K, l))