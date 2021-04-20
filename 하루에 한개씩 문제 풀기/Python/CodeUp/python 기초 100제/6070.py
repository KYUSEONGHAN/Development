import sys

month = int(sys.stdin.readline())

if month >= 3 and month <= 5:
    print('spring')
elif month >= 6 and month <= 8:
    print('summer')
elif month >= 9 and month <= 11:
    print('fall')
else:
    print('winter')