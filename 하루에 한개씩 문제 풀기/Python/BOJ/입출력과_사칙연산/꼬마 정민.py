# https://www.acmicpc.net/problem/11382
# boj, 11382: 꼬마 정민, python3
def solve(*args: tuple) -> int:
    return sum(args)

if __name__ == '__main__':
    a, b, c = map(int, input().split())

    print(solve(a, b, c))