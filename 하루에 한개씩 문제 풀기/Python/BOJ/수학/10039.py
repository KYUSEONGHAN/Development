# boj, 10039 : 평균 점수, python3
import sys

student = 5
student_num = []

for i in range(student):
    score = int(sys.stdin.readline())
#     score = int(input())
    if score >= 40:
        student_num.append(score)
    else:
        student_num.append(40)

result = sum(student_num) // student

print(result)