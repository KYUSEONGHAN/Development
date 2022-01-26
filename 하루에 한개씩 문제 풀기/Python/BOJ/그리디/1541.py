# boj, 1541: 잃어버린 괄호, python3
def solve(expression):
    split_num = expression.split('-')
    result = 0

    tmp = sum(map(int, (split_num[0].split('+'))))

    if expression[0] == '-':
        result -= tmp
    else:
        result += tmp

    for x in split_num[1:]:
        x = sum(map(int, (x.split('+'))))
        result -= x

    return result

if __name__ == '__main__':
    expression = str(input())  # 55-50+40

    print(solve(expression))