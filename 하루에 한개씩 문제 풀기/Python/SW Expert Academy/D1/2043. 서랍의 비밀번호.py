# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AV5QJ_8KAx8DFAUq&categoryId=AV5QJ_8KAx8DFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=1&pageSize=10&pageIndex=2
# sw expert academy, d1: 2043. 서랍의 비밀번호, python3
def solve(num1: int, num2: int) -> int:
    return num1 - num2 + 1

if __name__ == '__main__':
    p, k = map(int, input().split())

    print(solve(p, k))