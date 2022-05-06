# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AV5QFZtaAscDFAUq&categoryId=AV5QFZtaAscDFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=1&pageSize=10&pageIndex=2
# sw expert academy, d1: 2025. n줄 덧셈, python3
def solve(n: int) -> int:
    return sum(range(1, n+1))

if __name__ == '__main__':
    n = int(input())

    print(solve(n))