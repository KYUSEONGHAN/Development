# https://school.programmers.co.kr/learn/courses/30/lessons/120863
# programmers,level0: 다항식 더하기, python3
def join_polynomial(x_value: int, num_value: int) -> str:
    if not x_value and not num_value:
        return ''
    if not x_value:
        return str(num_value)
    if not num_value:
        return str(x_value) + 'x' if x_value != 1 else 'x'

    return f'{x_value}x + {num_value}' if x_value != 1 else f'x + {num_value}'

def solution(polynomial: str) -> str:
    split_polynomial = polynomial.replace(' ', '').split('+')
    nums, xs = [], []
    num_value, x_value = 0, 0

    for x in split_polynomial:
        if x[-1] == 'x':
            xs.append(x)
        else:
            nums.append(x)

    if xs:
        for x in xs:
            if x == 'x':
                x_value += 1
            else:
                x_value += int(x[:-1])

    if nums:
        for x in nums:
            num_value += int(x)


    return join_polynomial(x_value, num_value)

if __name__ == '__main__':
    print(solution("3x + 7 + x"))  # "4x + 7"
    print(solution("x + x + x"))   # "3x"
    print(solution("x"))