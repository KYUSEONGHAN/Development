# boj, 2753 : 윤년, python3
import sys

year = int(sys.stdin.readline())

if year%4==0 and (year%400==0 or year%100 is not 0):
    print(1)
else:
    print(0)