# https://school.programmers.co.kr/learn/courses/30/lessons/142086
# programmres, level0: 가장 가까운 같은 글자, python3
def solution(s: str) -> list:
    word, dict, answer = '', {}, []

    for index, x in enumerate(s):
        if x not in word:
            answer.append(-1)
        else:
            answer.append(index - dict[x])
        word += x
        dict[x] = index

    return answer

if __name__ == '__main__':
    print(solution("banana"))  # [-1, -1, -1, 2, 2, 2]
    print(solution("foobar"))  # [-1, -1, 1, -1, -1, -1]