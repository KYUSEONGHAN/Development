# https://www.acmicpc.net/problem/6778
# boj, 6778: which alien?, python3
import sys

input = sys.stdin.readline


def troymartian(num1: int, num2: int) -> bool:
    return True if 3 <= num1 and num2 <= 4 else False


def vladsaturnian(num1: int, num2: int) -> bool:
    return True if num1 <= 6 and 2 <= num2 else False


def graememercurian(num1: int, num2: int) -> bool:
    return True if num1 <= 2 and num2 <= 3 else False


def solve(num1: int, num2: int):
    if troymartian(num1, num2):
        print('TroyMartian')

    if vladsaturnian(num1, num2):
        print('VladSaturnian')

    if graememercurian(num1, num2):
        print('GraemeMercurian')


if __name__ == '__main__':
    num1 = int(input())
    num2 = int(input())

    solve(num1, num2)