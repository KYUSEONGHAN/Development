# boj, 1152 : 단어의 개수, python3
sentence = str(input())

if sentence == ' ':
    print(0)
else:
    sentence = sentence.strip(' ')

    sentence = sentence.split(' ')

    print(len(sentence))