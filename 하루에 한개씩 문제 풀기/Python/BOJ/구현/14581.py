# https://www.acmicpc.net/problem/14581
# boj, 14581: 팬들에게 둘러싸인 홍준, python3
def solve(id: str):
    print(':fan::fan::fan:')
    print(f':fan::{id}::fan:')
    print(':fan::fan::fan:')

if __name__ == '__main__':
    id = input()

    solve(id)