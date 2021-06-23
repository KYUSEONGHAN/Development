# programmers, phase1 : 최대공약수와 최소공배수, python
def gcd(x, y):
    while y:
        x , y = y, x % y
    return x

def lcm(x, y):
    return x * y // gcd(x, y)

def solution(n, m):
    return [gcd(n,m),lcm(n,m)]