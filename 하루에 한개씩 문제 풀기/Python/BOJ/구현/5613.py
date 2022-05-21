# https://www.acmicpc.net/problem/5613
# boj, 5613: 계산기 프로그램, python3
def calculate(l: list) -> int:
    result = 0

    for x in range(0, len(l), 2):
        if x == 0:
            if l[x+1] == '+':
                result += int(l[x]) + int(l[x+2])
            elif l[x+1] == '-':
                result += int(l[x]) - int(l[x + 2])
            elif l[x+1] == '*':
                result += int(l[x]) * int(l[x+2])
            elif l[x+1] == '/':
                result += int(l[x]) // int(l[x+2])
        else:
            if l[x+1] == '+':
                result += int(l[x+2])
            elif l[x+1] == '-':
                result -= int(l[x + 2])
            elif l[x+1] == '*':
                result *= int(l[x+2])
            elif l[x+1] == '/':
                result //= int(l[x+2])

    return result



if __name__ == '__main__':
    l = []

    while True:
        data = str(input())
        l.append(data)

        if data == '=':
            break

    print(calculate(l))