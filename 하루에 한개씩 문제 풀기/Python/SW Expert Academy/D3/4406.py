def solve(word: str) -> str:
    l = ['a', 'e', 'i', 'o', 'u']
    result = ''

    for x in word:
        if x not in l:
            result += x

    return result


T = int(input())

for test_case in range(1, T + 1):
    word = str(input())
    print(f'#{test_case} {solve(word)}')