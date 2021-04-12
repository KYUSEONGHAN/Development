#시간 초과 코드

# boj, 2869 : 달팽이는 올라가고 싶다. python3
import sys

A, B, V = map(int,sys.stdin.readline().split())
day = 0
m = 0

while True:
    day += 1
    m += A
    if m >= V:
        print(day)
        break
    else:
        m -= B

#수정 후 코드

import sys

A, B, V = map(int,sys.stdin.readline().split())

if (V-A)%(A-B) == 0:
    print(int((V-A)/(A-B))+1)
else:
    print(int((V-A)/(A-B))+2)