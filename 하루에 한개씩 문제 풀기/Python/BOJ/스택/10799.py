# boj, 10799: 쇠막대기, python3
def iron_bar(word):
    stack = []
    result = 0

    for x in range(len(word)):
        if word[x] == '(':
            stack.append(word[x])
        else:
            if word[x-1] == '(':
                stack.pop()
                result += len(stack)
            else:
                stack.pop()
                result += 1

    return result

if __name__ == '__main__':
    print(iron_bar(str(input())))