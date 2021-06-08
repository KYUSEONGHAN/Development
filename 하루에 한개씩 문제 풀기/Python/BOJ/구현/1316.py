# boj, 1316 : 그룹 단어 체커, python3
# 구현, 문자열 알고리즘
import sys


def checker(n):
    result = 0
    for _ in range(n):
        word = str(input())
        if list(word) == sorted(word, key=word.find):
            result += 1

    return result


N = int(sys.stdin.readline())

print(checker(N))