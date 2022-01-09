# boj, 10867: 중복 빼고 정렬하기, python3
import sys

def solve(nums):
    return sorted(set(nums))

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    nums = list(map(int, sys.stdin.readline().split()))

    print(*solve(nums))