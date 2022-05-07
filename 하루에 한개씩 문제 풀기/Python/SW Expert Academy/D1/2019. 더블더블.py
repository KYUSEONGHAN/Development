# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AV5QDEX6AqwDFAUq&categoryId=AV5QDEX6AqwDFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=1&pageSize=10&pageIndex=2
# sw expert academy, d1: 2019. 더블더블, python3
def solve(n: int) -> list:
    result = [1]

    for x in range(n):
        result.append(result[-1] * 2)

    return result
if __name__ == '__main__':
    n = int(input())

    print(*solve(n))