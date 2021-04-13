# boj, 2609 : 최대공약수와 최대공배수, python3
import sys
from math import gcd

def lcm(n1, n2):
    return n1 * n2 // gcd(n1, n2)

num1, num2 = map(int,sys.stdin.readline().split())

print(gcd(num1, num2))
print(lcm(num1, num2))