def study_alphabet(word: str) -> int:
    dict = {chr(x): index for index, x in enumerate(range(ord('a'), ord('z') + 1))}
    result = 0

    for index, x in enumerate(word):
        if dict[x] == index:
            result += 1
        else:
            break

    return result


T = int(input())

for test_case in range(1, T + 1):
    word = str(input())
    print(f'#{test_case} {study_alphabet(word)}')