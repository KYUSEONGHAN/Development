# 알람 시계
import sys

H, M = map(int,sys.stdin.readline().split())

if M >= 45:
    M -= 45
    print(H, M)
elif H == 0 and M < 45:
    H = 23
    M -= 45
    M += 60
    print(H, M)
else:
    H -= 1
    M -= 45
    M += 60
    print(H, M)