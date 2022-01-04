# boj, 3986: 좋은 단어, stack, python3
def good_word(word):
    stack = []

    for x in word:
        if not stack:
            stack.append(x)
            continue
        if x != stack[-1]:
            stack.append(x)
        elif x == stack[-1]:
            stack.pop()

    return 0 if stack else 1

def solution(N):
    return sum([good_word(str(input())) for _ in range(N)])

if __name__ == '__main__':
    N = int(input())

    print(solution(N))