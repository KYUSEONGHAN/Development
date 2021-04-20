import sys

num = int(sys.stdin.readline())

if num < 0 and num %2 == 0:
    print('A')
elif num < 0 and num %2 != 0:
    print('B')
elif num > 0 and num %2 == 0:
    print('C')
else:
    print('D')