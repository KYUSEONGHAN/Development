# boj, 3036 : 링, python3
# 정수론 및 조합론
import sys

def gcd(x,y):
    while y:
        x, y = y, x%y
    return x

def lcm(x,y):
    return x*y // gcd(x,y)

def solve(num1, num2):
    print('%d/%d' %(lcm(num1,num2)//num2, lcm(num1,num2)//num1))

N = int(sys.stdin.readline())
cricle_list = list(map(int, sys.stdin.readline().split()))

for i in range(N-1):
    solve(cricle_list[0],cricle_list[i+1])
