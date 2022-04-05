# https://www.acmicpc.net/problem/19564
# boj, 19564: 반복, python3
def solve(word: str) -> int:
    return sum([1 for x in range(1, len(word)) if word[x] <= word[x-1]]) + 1

if __name__ == '__main__':
    s = str(input())

    print(solve(s))