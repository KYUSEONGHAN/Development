# boj, 1157 : 단어 공부, python3
from collections import Counter


def most_common(word):
    word = word.lower()
    c = Counter(word)
    nums = c.most_common()
    maximum = nums[0][1]

    result = [num[0] for num in nums if num[1] == maximum]

    return result[0].upper() if len(result) == 1 else '?'


word = str(input())

print(most_common(word))