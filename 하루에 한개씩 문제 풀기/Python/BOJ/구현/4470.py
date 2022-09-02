# https://www.acmicpc.net/problem/4470
# boj, 4470: 줄번호, python3
def solve(index: int, word: str) -> str:
    return f'{index}. {word}'

if __name__ == '__main__':
    n = int(input())

    for index in range(1, n+1):
        word = str(input())

        print(solve(index, word))