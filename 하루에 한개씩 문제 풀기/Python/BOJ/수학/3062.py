# https://www.acmicpc.net/problem/3062
# boj, 3062: 수 뒤집기, python3
def solve(num: str) -> str:
    reverse_num = str(int(num) + int(num[::-1]))
    return 'YES' if reverse_num == reverse_num[::-1] else 'NO'

if __name__ == '__main__':
    n = int(input())

    for _ in range(n):
        num = str(input())

        print(solve(num))