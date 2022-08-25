# https://www.acmicpc.net/problem/9086
# boj, 9086: 문자열, python3
def solve(word: str) -> str:
    return word[0] + word[-1]

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        word = str(input())

        print(solve(word))