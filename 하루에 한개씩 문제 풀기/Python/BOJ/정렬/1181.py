# boj, 1181 : 단어 정렬, python3
N = int(input())
word = []

for _ in range(N):
    word.append(input())

word = list(set(word))
word.sort(key=lambda x : (len(x),x))

print("\n".join(word))