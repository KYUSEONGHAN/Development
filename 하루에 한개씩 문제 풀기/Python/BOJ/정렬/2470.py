# boj, 2470: 두 용액, python3
import sys

def solve(n, l):
    left, right = 0, n-1
    x, y = left, right
    num1 = l[left] + l[right]

    while left < right:
        num2 = l[left] + l[right]

        if abs(num2) < abs(num1):
            num1 = num2
            x, y = left, right

            if num1 == 0:
                break

        if num2 < 0:
            left += 1
        else:
            right -= 1

    return l[x], l[y]

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    solution = sorted(map(int, sys.stdin.readline().split()))

    print(*solve(n, solution))