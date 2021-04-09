# boj, 1712 : 손익분기점, python3
A, B, C = map(int,input().split())

cnt = 0

while True:
    if C * cnt > A + (B * cnt):
        print(cnt)
        break
    elif B >= C:
        print(-1)
        break
    else:
        cnt += 1

#(sol2)

A, B, C = map(int,input().split())

while True:
    if B >= C:
       print(-1)
       break
    else:
       print(A//(C-B)+1)
       break