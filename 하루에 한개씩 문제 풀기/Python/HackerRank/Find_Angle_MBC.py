# hackerRank, Find Angle MBC, python3
import math
import sys

def solution(y, x):
    return str(round(math.atan2(y, x) * 180 / PI)) + '°'

if __name__ == "__main__":
    PI = 3.1415926535
    y = int(sys.stdin.readline())
    x = int(sys.stdin.readline())

    print(solution(y, x))


# source == https://www.hackerrank.com/challenges/find-angle/problem