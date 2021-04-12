# boj, 2437 : 저울, python3
import sys

N = int(sys.stdin.readline())

if N > 1000 or N < 1:
    print("N range error")
else:
    w = list(map(int,sys.stdin.readline().split()))
    if N != len(w):
        print("error")
    else:
        w.sort()
        result = 1
        for i in w:
            if result < i:
                break
            result += i
        print(result)