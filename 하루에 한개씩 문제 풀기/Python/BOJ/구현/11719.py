# boj, 11719: 그대로 출력하기2, python3
import sys

input = sys.stdin.readline

if __name__ == '__main__':
    for _ in range(100):
        word = input().rstrip('\n')
        print(word)