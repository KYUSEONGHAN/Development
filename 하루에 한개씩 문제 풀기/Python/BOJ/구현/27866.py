# https://www.acmicpc.net/problem/27866
# boj, 27866: 문자와 문자열, python3
def solve(s: str, i: int) -> str:
    return s[i-1]

if __name__ == '__main__':
    s = input()
    i = int(input())

    print(solve(s, i))