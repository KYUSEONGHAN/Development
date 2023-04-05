# https://www.acmicpc.net/problem/4101
# boj, 4101: 크냐?, python3
def solve(a: int, b: int) -> str:
    return 'Yes' if a > b else 'No'

if __name__ == '__main__':
    while True:
        a, b = map(int, input().split())

        if a == 0 and b == 0:
            break

        print(solve(a, b))