# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AV5QPRjqA10DFAUq&categoryId=AV5QPRjqA10DFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=1&pageSize=10&pageIndex=1
# sw expert academy, d1: 2058. 자릿수 더하기, python3
def solve(n: str) -> int:
    return sum(list(map(int, str(n))))

if __name__ == '__main__':
    n = str(input())

    print(solve(n))