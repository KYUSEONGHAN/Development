# https://swexpertacademy.com/main/solvingProblem/solvingProblem.do
# sw expert academy, d2: 1926. 간단한 369게임, python3
import sys

input = sys.stdin.readline

def solve(n: int) -> list:
    nums = [str(x) for x in range(1, n+1)]

    for x in range(n):
        trans = ''
        for y in nums[x]:
            if y in ['3', '6', '9']:
                trans += '-'
                nums[x] = trans

    return nums

if __name__ == '__main__':
    n = int(input())

    print(*solve(n))