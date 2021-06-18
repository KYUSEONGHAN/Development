# boj, 10162 : 전자레인지, python3
# 그리디 알고리즘
import sys


def microwave(time):
    result = [0, 0, 0]  # 300s, 60s, 10s
    button = [300, 60, 10]

    if time % 10 != 0:
        return -1

    for i in range(len(button)):
        result[i] += time // button[i]
        time %= button[i]

    return ' '.join(map(str, result))


T = int(sys.stdin.readline())

print(microwave(T))