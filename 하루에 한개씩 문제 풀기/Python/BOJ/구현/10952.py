# boj, 10952 : A + B -5, python3
while True:
    A, B = map(int,input().split())
    if (A,B) == (0,0):
        break
    else:
        print(sum((A,B)))