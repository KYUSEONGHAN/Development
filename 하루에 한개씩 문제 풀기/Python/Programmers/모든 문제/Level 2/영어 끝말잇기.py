# https://school.programmers.co.kr/learn/courses/30/lessons/12981
# programmers, level2: 영어 끝말잇기, python3
def solution(n: int, words: list) -> list:
    dict, tmp, answer = {}, '', []

    for index, word in enumerate(words):
        if not tmp:
            tmp = word
            dict[word] = 1
            continue
        if tmp[-1] != word[0] or word in dict:
            answer = [index % n +1, index // n + 1]
            break

        dict[word] = 1
        tmp = word

    return answer if answer else [0, 0]

if __name__ == '__main__':
    print(solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))  # [3, 3]
    print(solution(5, ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]))  # [0, 0]
    print(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]))  # [1, 3]
    print(solution(2, ['land', 'dream', 'mom', 'mom', 'ror']))  # [2, 2]
    print(solution(2, ['land', 'dream', 'mom', 'mom']))   # [2, 2]