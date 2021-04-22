# codeup, 1420 : 3등 찾기, python3
import sys


def sort_score(n):
    student = []

    for i in range(n):
        name, score = input().split()
        score = int(score)
        student.append([name, score])

    result = sorted(student, key=lambda x: x[1], reverse=True)

    return result[2][0]


n = int(sys.stdin.readline())

print(sort_score(n))