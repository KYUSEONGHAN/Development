# https://www.acmicpc.net/problem/5597
# boj, 5597: 과제 안 내신 분..?, python3
import sys

input = sys.stdin.readline

def solve(nums: set) -> str:
    return '\n'.join(map(str, sorted({x for x in range(1, 30+1)} - nums)))

if __name__ == '__main__':
    student_nums = {int(input()) for _ in range(28)}

    print(solve(student_nums))