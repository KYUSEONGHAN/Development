# boj, 11656:접미사 배열, python3
def solution(word):
    return '\n'.join(sorted([word[x:] for x in range(len(word))]))

if __name__ == '__main__':
    s = str(input())  # baekjoon

    print(solution(s))