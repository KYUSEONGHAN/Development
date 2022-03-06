# https://www.acmicpc.net/problem/4949
# boj, 4949: 균형잡힌 세상, python3

def solve(word):
    stack = []

    for x in word:
        if x == '(' or x == '[':
            stack.append(x)
        elif x == ')':
            if stack:
                bracket = stack.pop()
                if bracket != '(':
                    return 'no'
            else:
                return 'no'
        elif x == ']':
            if stack:
                bracket = stack.pop()
                if bracket != '[':
                    return 'no'
            else:
                return 'no'

    return 'yes' if not stack else 'no'

while True:
    word = str(input().split('.')[0])

    if not word:
        break

    print(solve(word))


