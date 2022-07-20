# https://www.acmicpc.net/problem/25372
# boj, 25372: 성택이의 은밀한 비밀번호, python3

def solve(word: str) -> str:
    return 'yes' if len(word)>=6 and len(word)<=9 else 'no'

if __name__ == '__main__':
    n = int(input())

    for _ in range(n):
        word = input()

        print(solve(word))