# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AV2gbY0qAAQBBAS0&categoryId=AV2gbY0qAAQBBAS0&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=1&pageSize=10&pageIndex=2
# sw expert academy, d1: 1545. 거꾸로 출력해 보아요, python3
def solve(n: int) -> list:
    return [x for x in range(n, -1, -1)]

if __name__ == '__main__':
    n = int(input())

    print(*solve(n))