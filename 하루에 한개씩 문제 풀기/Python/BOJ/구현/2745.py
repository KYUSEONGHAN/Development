# https://www.acmicpc.net/problem/2745
# boj, 2745: 진법 변환, python3
def solve(n: str, b: str) -> int:
    b = int(b)
    res = 0
    for idx, item in enumerate(n):
        try:
            if int(item):
                res += int(item) * b ** (len(n) - 1 - idx)
        except:
            res += (ord(item) - 55) * b ** (len(n) - 1 - idx)
    return res

if __name__ == '__main__':
    n, b = str(input()).split()

    print(solve(n, b))