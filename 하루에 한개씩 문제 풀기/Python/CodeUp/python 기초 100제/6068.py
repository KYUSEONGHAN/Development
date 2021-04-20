import sys

score = int(sys.stdin.readline())

if score >= 90 and score <= 100:
    print('A')
elif score >= 70 and score <= 89:
    print('B')
elif score >= 40 and score <= 69:
    print('C')
else :
    print('D') 