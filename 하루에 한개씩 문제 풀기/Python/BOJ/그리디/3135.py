# boj, 3135: 라디오, python3
import sys

input = sys.stdin.readline

def solve(start, end, l):
    if end in l:
        return 1

    near_l = []
    result = 0

    for x in l:
        near_l.append(abs(end - x))

    near_num = min(near_l)

    if abs(end-start) <= near_num:
        near_num = abs(end-start)
    else:
        result += 1

    while near_num != 0:
        near_num -= 1
        result += 1

    return result

if __name__ == '__main__':
    a, b = map(int, input().split())
    n = int(input())
    frequency = [int(input()) for _ in range(n)]

    print(solve(a, b, frequency))