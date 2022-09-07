# https://www.acmicpc.net/problem/4740
# boj, 4740: 거울, 오! 거울, python3
def solve(word: str) -> str:
    return word[::-1]

if __name__ == '__main__':
    while True:
        word = str(input())

        if word == '***':
            break

        print(solve(word))