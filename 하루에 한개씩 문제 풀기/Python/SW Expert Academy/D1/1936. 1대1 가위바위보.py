# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PjKXKALcDFAUq&categoryId=AV5PjKXKALcDFAUq&categoryType=CODE&problemTitle=&orderBy=PASS_RATE&selectCodeLang=PYTHON&select-1=&pageSize=10&pageIndex=1
# sw expert academy, d1: 1936. 1대 1 가위바위보, python3

def solve(a: int, b: int) -> str:
    # a가 가위일때
    if a == 1:
        return 'B' if b == 2 else 'A'
    # a가 바위일때
    elif a == 2:
        return 'A' if b == 1 else 'B'
    # a가 보일때
    else:
        return 'B' if a == 1 else 'A'

if __name__ == '__main__':
    a, b = map(int, input().split())

    print(solve(a, b))