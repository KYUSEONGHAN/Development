# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AV5QGNvKAtEDFAUq&categoryId=AV5QGNvKAtEDFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=1&pageSize=10&pageIndex=2
# sw expert academy, d1: 2029. 몫과 나머지 출력하기, python3
def solve(num1: int, num2: int) -> str:
    return ' '.join(map(str, (num1 // num2, num1 % num2)))

if __name__ == '__main__':
    t = int(input())

    for i in range(1, t+1):
        a, b = map(int, input().split())

        print(f'#{i} {solve(a, b)}')