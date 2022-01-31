# boj, 18108: 1998년생인 내가 태국에서는 2541년생?!, python3
import sys

input = sys.stdin.readline

def solve(year):
    return year - 543

if __name__ == '__main__':
    year = int(input())

    print(solve(year))