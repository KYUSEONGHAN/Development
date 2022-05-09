# https://www.acmicpc.net/problem/1550
# boj, 1550: 16진수, python3
def solve(data: str) -> int:
    return int(data, 16)

if __name__ == '__main__':
    input_data = input()

    print(solve(input_data))
