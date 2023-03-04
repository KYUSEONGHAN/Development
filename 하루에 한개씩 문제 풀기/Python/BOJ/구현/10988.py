# https://www.acmicpc.net/problem/10988
# boj, 10988: 팰린드롬인지 확인하기, python3
def solve(word: str) -> int:
    return 1 if word == word[::-1] else 0

if __name__ == '__main__':
    word = str(input())

    print(solve(word))