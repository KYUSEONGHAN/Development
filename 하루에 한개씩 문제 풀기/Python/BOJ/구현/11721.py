# https://www.acmicpc.net/problem/11721
# boj, 11721: 열 개씩 끊어 출력하기, python3
import sys

input = sys.stdin.readline

def solve(word):
    tmp = 0
    for x in range(0, len(word), 10):
        print(word[tmp:x+10])
        tmp = x+10

if __name__ == '__main__':
    word = str(input())

    solve(word)