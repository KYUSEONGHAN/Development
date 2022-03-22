# https://www.acmicpc.net/problem/13163
# boj, 13163: 닉네임에 갓 붙이기, python3
def solve(name: list) -> str:
    result = ''

    for x in name[1:]:
        result += x

    return 'god' + result

if __name__ == '__main__':
    n = int(input())

    for _ in range(n):
        name = list(map(str, input().split()))

        print(solve(name))
