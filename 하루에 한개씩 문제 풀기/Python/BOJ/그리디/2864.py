# boj, 2864: 5와 6의 차이, python3
def solve(num1, num2):
    min_num1, max_num1 = '', ''
    min_num2, max_num2 = '', ''

    for x in num1:
        if x == '5':
            min_num1 += x
            max_num1 += '6'
        elif x == '6':
            min_num1 += '5'
            max_num1 += x
        else:
            min_num1 += x
            max_num1 += x

    for x in num2:
        if x == '5':
            min_num2 += x
            max_num2 += '6'
        elif x == '6':
            min_num2 += '5'
            max_num2 += x
        else:
            min_num2 += x
            max_num2 += x

    min_sum = int(min_num1) + int(min_num2)
    max_sum = int(max_num1) + int(max_num2)

    return min_sum, max_sum

if __name__ == '__main__':
    a, b = map(str, input().split())

    print(*solve(a, b))