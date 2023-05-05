def solve(word: str, sentence: str) -> int:
    return sentence.count(word)

for _ in range(10):
    T = int(input())
    word = str(input())
    sentence = str(input())
    print(f'#{T} {solve(word, sentence)}')