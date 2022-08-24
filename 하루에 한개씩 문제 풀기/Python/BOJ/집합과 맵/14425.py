# https://www.acmicpc.net/problem/14425
# boj, 14425: 문자열 집합, python3
def solve(s: list, data_m: list) -> int:
    result = 0

    for x in s:
        if x in data_m:
            for y in data_m:
                if x == y:
                    result += 1

    return result

if __name__ == '__main__':
    n, m = map(int, input().split())
    s = [str(input()) for _ in range(n)]
    data_m = [str(input()) for _ in range(m)]

    print(solve(s, data_m))