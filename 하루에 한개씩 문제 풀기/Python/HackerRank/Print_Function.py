# hackerRank, print function, python
import sys


def solution(n):
    return ''.join(map(str, list(range(1, n + 1))))


if __name__ == '__main__':
    n = int(sys.stdin.readline())

    print(solution(n))