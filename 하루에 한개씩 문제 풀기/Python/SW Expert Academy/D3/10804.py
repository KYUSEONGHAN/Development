def str_mirror(word: str) -> str:
    dict = {"b": "d", "d": "b", "p": "q", "q": "p"}

    return ''.join(map(str, [dict[x] for x in word[::-1]]))


T = int(input())

for test_case in range(1, T + 1):
    word = str(input())
    print(f'#{test_case} {str_mirror(word)}')