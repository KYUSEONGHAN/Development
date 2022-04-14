# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AV5QQ6qqA40DFAUq&categoryId=AV5QQ6qqA40DFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=1&pageSize=10&pageIndex=1
# sw expert academy, d1: 2070. 큰 놈, 작은 놈, 같은 놈, python3
def solve(num1: int, num2: int) -> str:
    if num1 == num2:
        return '='
    return '>' if num1 > num2 else '<'

if __name__ == '__main__':
    t = int(input())

    for i in range(1, t+1):
        num1, num2 = map(int, input().split())
        print('#' + str(i) + ' ' + solve(num1, num2))