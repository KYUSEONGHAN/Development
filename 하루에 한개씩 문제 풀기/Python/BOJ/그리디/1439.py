# boj, 1439 : 뒤집기, python
# 그리디 알고리즘
def solution(word):
    result = [0, 0]

    if word[0] == '0':
        result[0] += 1
    else:
        result[1] += 1

    for i in range(len(word) - 1):
        if word[i] != word[i + 1]:
            if word[i + 1] == '0':
                result[0] += 1
            else:
                result[1] += 1

    return min(result)


S = list(str(input()))

print(solution(S))