# codeup, 3120 : 리모컨, python3
import sys

def remocon(a, b):
    result = 0

    if a < b:
        a, b = b, a
    target = a - b

    while True:
        if target == 0:
            return result
        elif target > 7:
            target -= 10
        elif target > 3:
            target -= 5
        elif target >= 1:
            target -= 1
        elif target < 0:
            target *= -1
            result -= 1

        result += 1


if __name__ == '__main__':
    a, b = map(int, sys.stdin.readline().split())

    print(remocon(a, b))