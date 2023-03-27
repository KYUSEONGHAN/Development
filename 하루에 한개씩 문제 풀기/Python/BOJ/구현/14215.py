# https://www.acmicpc.net/problem/14215
# boj, 14315: 세 막대, Python3
def solve(*args: tuple) -> int:
    sort_a, sort_b, sort_c = sorted(args)

    if sort_a + sort_b > sort_c:
        return sort_a + sort_b + sort_c

    return (sort_a + sort_b) * 2 - 1


if __name__ == '__main__':
    a, b, c = map(int, input().split())

    print(solve(a, b, c))