# boj, 10951 : a + b - 4, python3
while True:
    try:
        A, B = map(int,input().split())
        print(sum((A,B)))
    except:
        break