# boj, 10250: ACM호텔, python3
import sys

input = sys.stdin.readline

def solve(data):
    result = []

    for x in data:
        h, w, n = x[0], x[1], x[2]

        if n % h == 0:
            result.append(h*100 + (n//h))
        else:
            result.append((n%h)*100 + (n//h)+1)

    return '\n'.join(map(str, result))

if __name__ == '__main__':
    t = int(input())
    data = [list(map(int, input().split())) for _ in range(t)]

    print(solve(data))