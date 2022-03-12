# https://www.acmicpc.net/problem/9093
# boj, 9093: 단어 뒤집기, python3
def solve(word):
    result = ''

    for x in word:
        result += x[::-1] + ' '

    return result[:-1]


if __name__ == '__main__':
    t = int(input())
    words = [list(map(str, input().split())) for _ in range(t)]

    for word in words:
        print(solve(word))
