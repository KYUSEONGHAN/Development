def lonely_word(word: str) -> str:
    dict, result = {}, []

    for x in word:
        if x not in dict:
            dict[x] = 1
        else:
            dict[x] += 1

    for key, value in dict.items():
        if value % 2 == 1:
            result.append(key)

    return ''.join(map(str, sorted(result))) if result else 'Good'


T = int(input())

for test_case in range(1, T + 1):
    word = str(input())
    print(f'#{test_case} {lonely_word(word)}')